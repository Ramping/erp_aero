import pypdf
from pathlib import Path
from utils import path_generator as pg

print(pg.main_file_path('test_task.pdf'))
print(pg.list_checked_files())
def read_reference_pdf(pdffiledata):
    if Path(pdffiledata.reference_file).suffix == '.pdf':
        with open(pg.main_file_path(pdffiledata.reference_file), 'rb') as file:
            pdf = pypdf.PdfReader(file)
            return pdf.pages[0].extract_text()
    else:
        return ValueError(f'{pdffiledata.reference_file} - Invalid file format')


def read_check_pdf(file_name):
    if Path(file_name).suffix == '.pdf':
        with open(file_name, 'rb') as file:
            pdf = pypdf.PdfReader(file)
            return pdf.pages[0].extract_text()
    else:
        return ValueError(f'{file_name} - Invalid file format')
