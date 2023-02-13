import pypdf
from pathlib import Path
from utils import path_generator as pg


def read_reference_pdf(pdffiledata):
    if Path(pdffiledata.reference_file).suffix == '.pdf':
        with open(pg.main_file_path(pdffiledata.reference_file), 'rb') as file:
            pdf = pypdf.PdfReader(file)
            return pdf.pages[0].extract_text()
    else:
        return ValueError(f'{pdffiledata.reference_file} - Invalid file format')


def read_check_pdf(file):
    if Path(pg.checked_file(file)).suffix == '.pdf':
        with open(pg.checked_file(file), 'rb') as file:
            pdf = pypdf.PdfReader(file)
            return pdf.pages[0].extract_text()
    else:
        raise ValueError(f'{file} - Invalid file format')

