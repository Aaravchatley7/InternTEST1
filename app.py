from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
import os
from langgraph_flow import run_langgraph_workflow
from email_utils import send_email
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        aadhaar_number = request.form['aadhaar']
        pan_number = request.form['pan']

        aadhaar_file = request.files.get('aadhaar_file')
        pan_file = request.files.get('pan_file')

        if (not aadhaar_file or aadhaar_file.filename == '') and (not pan_file or pan_file.filename == ''):
            flash('Please upload at least Aadhaar or PAN document.')
            return redirect(request.url)

        aadhaar_path = None
        pan_path = None

        if aadhaar_file and allowed_file(aadhaar_file.filename):
            aadhaar_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(aadhaar_file.filename))
            aadhaar_file.save(aadhaar_path)

        if pan_file and allowed_file(pan_file.filename):
            pan_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(pan_file.filename))
            pan_file.save(pan_path)

        send_email(email, "Documents Received", "We received your details and will process your documents shortly.")

        form_data = {
            "name": name,
            "phone": phone,
            "email": email,
            "aadhaar_number": aadhaar_number,
            "pan_number": pan_number
        }

        document_paths = {
            "aadhaar_image": aadhaar_path,
            "pan_image": pan_path
        }

        run_langgraph_workflow(form_data, document_paths)


        flash('Form submitted. Check your email for updates.')
        return redirect('/')

    return render_template('form.html')
if __name__ == "__main__":
    app.run(debug=True)
