from PyPDF2 import PdfReader, PdfWriter
import os

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
