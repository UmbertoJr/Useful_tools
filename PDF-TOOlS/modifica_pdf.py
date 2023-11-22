import PyPDF2

def estrai_pagine(input_filename, output_filename, start_page, end_page):
    # Crea un nuovo oggetto PDF
    pdf_writer = PyPDF2.PdfWriter()

    # Apri il file PDF originale
    with open(input_filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)

        # Assicurati che l'intervallo di pagine sia valido
        if start_page <= end_page and 0 <= start_page < len(pdf_reader.pages) and 0 <= end_page < len(pdf_reader.pages):
            # Per ogni pagina nell'intervallo desiderato
            for page_num in range(start_page, end_page+1):
                # Ottieni la pagina e aggiungila al nuovo PDF
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

            # Scrivi il nuovo PDF
            with open(output_filename, 'wb') as output:
                pdf_writer.write(output)
        else:
            print("Intervallo di pagine non valido.")


def ruota_pdf(input_filename, output_filename, gradi=180):
    # Crea un nuovo oggetto PDF
    pdf_writer = PyPDF2.PdfWriter()

    # Apri il file PDF originale
    with open(input_filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)

        # Per ogni pagina nel PDF
        for page_num in range(len(pdf_reader.pages)):
            # Ottieni la pagina
            page = pdf_reader.pages[page_num]

            # Ruota la pagina di 90 gradi
            page.rotate(gradi)

            # Aggiungi la pagina modificata al nuovo PDF
            pdf_writer.add_page(page)

        # Scrivi il nuovo PDF modificato
        with open(output_filename, 'wb') as output:
            pdf_writer.write(output)

# Esempi di utilizzo
# estrai_pagine('input.pdf', 'output.pdf', 1, 3)
# ruota_pdf('input.pdf', 'output.pdf', 90)
from PyPDF2 import PdfMerger

def concat_pdfs(pdf_list, output_path):
    merger = PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()

    return output_path

# Example usage:
# Specify the PDF files to merge
pdf_files = ['./Immatricolazione', 'file2.pdf', 'file3.pdf']
# Specify the output file path
output_file = 'merged_document.pdf'

# Call the function with the list of PDF files
merged_pdf_path = concat_pdfs(pdf_files, output_file)

print(f"PDF files have been merged into {merged_pdf_path}")

