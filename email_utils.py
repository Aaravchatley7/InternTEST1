import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SMTP_EMAIL, SMTP_PASSWORD

def send_email(recipient, subject, body_text, body_html=None):
    """Send an email with optional HTML body."""
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = f"DocVerify System <{SMTP_EMAIL}>"
        msg['To'] = recipient

        part1 = MIMEText(body_text, 'plain')
        msg.attach(part1)

        if body_html:
            part2 = MIMEText(body_html, 'html')
            msg.attach(part2)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SMTP_EMAIL, SMTP_PASSWORD)
            smtp.send_message(msg)

        print(f"[EMAIL] Sent to {recipient}: {subject}")
        return True
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")
        return False

def build_verification_email(form_data, result):
    """Build a rich HTML email for verification result."""
    name = form_data.get("name", "User")
    is_match = result.get("match", False)
    fields = result.get("fields", {})

    status_color = "#16a34a" if is_match else "#dc2626"
    status_text = "VERIFIED ✓" if is_match else "FAILED ✗"
    status_bg = "#f0fdf4" if is_match else "#fef2f2"

    rows = ""
    field_labels = {
        "name": "Full Name",
        "dob": "Date of Birth",
        "aadhaar": "Aadhaar Number",
        "pan": "PAN Number",
        "phone": "Phone Number"
    }
    for key, label in field_labels.items():
        if key in fields:
            f = fields[key]
            icon = "✓" if f["match"] else "✗"
            color = "#16a34a" if f["match"] else "#dc2626"
            rows += f"""
            <tr>
                <td style="padding:10px;border-bottom:1px solid #e5e7eb;color:#6b7280">{label}</td>
                <td style="padding:10px;border-bottom:1px solid #e5e7eb">{f['form_value']}</td>
                <td style="padding:10px;border-bottom:1px solid #e5e7eb">{f['doc_value']}</td>
                <td style="padding:10px;border-bottom:1px solid #e5e7eb;color:{color};font-weight:bold">{icon}</td>
            </tr>"""

    html = f"""
    <html><body style="font-family:Arial,sans-serif;background:#f9fafb;padding:32px">
    <div style="max-width:600px;margin:0 auto;background:white;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08)">
        <div style="background:{status_color};padding:32px;text-align:center">
            <h1 style="color:white;margin:0;font-size:28px">DocVerify</h1>
            <p style="color:rgba(255,255,255,0.85);margin:8px 0 0">Document Verification System</p>
        </div>
        <div style="padding:32px">
            <p style="color:#374151">Dear <strong>{name}</strong>,</p>
            <div style="background:{status_bg};border:2px solid {status_color};border-radius:12px;padding:20px;text-align:center;margin:20px 0">
                <div style="font-size:36px;font-weight:900;color:{status_color}">{status_text}</div>
                <p style="color:#374151;margin:8px 0 0">{'Your identity documents have been successfully verified.' if is_match else 'Document verification failed. One or more fields did not match.'}</p>
            </div>
            <h3 style="color:#111827;border-bottom:2px solid #f3f4f6;padding-bottom:12px">Verification Details</h3>
            <table style="width:100%;border-collapse:collapse">
                <thead>
                    <tr style="background:#f9fafb">
                        <th style="padding:10px;text-align:left;color:#374151">Field</th>
                        <th style="padding:10px;text-align:left;color:#374151">Submitted</th>
                        <th style="padding:10px;text-align:left;color:#374151">From Document</th>
                        <th style="padding:10px;text-align:left;color:#374151">Status</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
            {'<p style="color:#dc2626;margin-top:20px">⚠️ Please re-submit with correct details or valid documents.</p>' if not is_match else ''}
        </div>
        <div style="background:#f9fafb;padding:20px;text-align:center;color:#9ca3af;font-size:12px">
            DocVerify — Automated Document Verification System
        </div>
    </div>
    </body></html>"""

    text = f"""DocVerify — Document Verification Result\n\nDear {name},\n\nStatus: {status_text}\n\n{'Documents verified successfully.' if is_match else 'Verification failed. Please re-submit.'}\n\nField Details:\n"""
    for key, label in field_labels.items():
        if key in fields:
            f = fields[key]
            text += f"  {label}: {'✓' if f['match'] else '✗'} (Submitted: {f['form_value']}, Document: {f['doc_value']})\n"

    return text, html
