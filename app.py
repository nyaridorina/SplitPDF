from flask import Flask, request, send_file, render_template_string
from PyPDF2 import PdfReader, PdfWriter
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <title>PDF Divider</title>
    <h1>Upload a PDF to divide it into individual pages</h1>
    <form method=post enctype=multipart/form-data action="/upload">
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        split_pdf(filepath)
        return f'PDF split successfully. The individual pages are saved in the folder: {os.path.dirname(filepath)}'
        return f'PDF split successfully. The individual pages are saved in the same folder: {UPLOAD_FOLDER}'

def split_pdf(filepath):
    pdf = PdfReader(filepath)
    base_filename = os.path.splitext(os.path.basename(filepath))[0]
    output_folder = os.path.dirname(filepath)  # Use the same directory as the uploaded file
    
    for page_number in range(len(pdf.pages)):
        writer = PdfWriter()
        writer.add_page(pdf.pages[page_number])
        output_filename = os.path.join(output_folder, f"{base_filename}_p{page_number + 1}.pdf")
        with open(output_filename, 'wb') as output_pdf:
            writer.write(output_pdf)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
