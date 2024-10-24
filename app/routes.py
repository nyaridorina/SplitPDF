from flask import Blueprint, request, render_template, current_app
from .utils import split_pdf
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        split_pdf(filepath)
        return f'PDF split successfully. The individual pages are saved in the folder: {os.path.dirname(filepath)}'
