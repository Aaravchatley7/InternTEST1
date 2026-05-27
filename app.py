"""
app.py — Flask application entry point.
"""

import os
import re
import uuid
import traceback
from flask import Flask, render_template, request, redirect, flash, session, url_for
from werkzeug.utils import secure_filename

from langgraph_flow import run_langgraph_workflow
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'bmp', 'tiff'}


def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_upload(file_obj, prefix: str) -> str:
    ext = file_obj.filename.rsplit('.', 1)[-1].lower()
    name = secure_filename(f"{prefix}_{uuid.uuid4().hex[:10]}.{ext}")
    path = os.path.join(UPLOAD_FOLDER, name)
    file_obj.save(path)
    return path


@app.route('/', methods=['GET', 'POST'])
def index():
    result    = session.pop('verification_result', None)
    form_data = session.pop('form_data', None)

    if request.method == 'POST':
        # Collect form fields
        aadhaar_raw = re.sub(r'[\s\-]', '', request.form.get('aadhaar', '').strip())
        form_data = {
            'name':           request.form.get('name',  '').strip(),
            'dob':            request.form.get('dob',   '').strip(),
            'phone':          request.form.get('phone', '').strip(),
            'email':          request.form.get('email', '').strip(),
            'aadhaar_number': aadhaar_raw,
            'pan_number':     request.form.get('pan',   '').strip().upper(),
        }

        if not form_data['name']:
            flash('Full name is required.', 'error')
            session['form_data'] = form_data
            return redirect(url_for('index'))

        # Collect uploaded files
        document_paths = {}
        for field, (path_key, prefix) in [
            ('aadhaar_file',  ('aadhaar_image',  'aadhaar')),
            ('pan_file',      ('pan_image',       'pan')),
            ('passport_file', ('passport_image',  'passport')),
        ]:
            f = request.files.get(field)
            if f and f.filename and allowed_file(f.filename):
                document_paths[path_key] = save_upload(f, prefix)

        if not document_paths:
            flash('Please upload at least one document image (Aadhaar, PAN, or Passport).', 'error')
            session['form_data'] = form_data
            return redirect(url_for('index'))

        # Run pipeline
        try:
            result = run_langgraph_workflow(form_data, document_paths)
            session['verification_result'] = result
            session['form_data'] = form_data
        except Exception as e:
            print(f"[APP] Pipeline error: {e}")
            traceback.print_exc()
            flash(f'Verification error: {e}', 'error')
            session['form_data'] = form_data

        return redirect(url_for('index'))

    return render_template('form.html', result=result, form_data=form_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
