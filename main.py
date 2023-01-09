import PyPDF2
from pathlib import Path


def read_pdf(pdf_file: str) -> dict:
    if Path(pdf_file).suffix == '.pdf':
        key_list = [
            'PN:', 'SN:', 'DESCRIPTION:', 'LOCATION:', 'CONDITION:', 'RECEIVER#:', 'UOM:', 'EXP DATE:', 'PO:', 'CERT SOURCE:',
            'REC.DATE:', 'MFG:', 'BATCH# :', 'DOM:', 'REMARK:', 'LOT# :', 'TAGGED BY:', 'Qty:', 'NOTES:'
        ]
        # Opening a file in read mode
        with open(pdf_file, 'rb') as file:
            # Create a PDF object
            pdf = PyPDF2.PdfReader(file)
            # Creating a dictionary to store information
            data = {}
            # Extracting text from an object
            text = pdf.pages[0].extract_text()
            # In a loop, using a pre-prepared list, parse the received text from PDF and fill the dictionary
            for index, key in enumerate(key_list):
                formatted_key = key.replace(':', '').strip()
                if index+1 < len(key_list):
                    value = text[text.find(key)+len(key):text.find(key_list[index+1])]
                    data[formatted_key] = value.replace('\n', '').strip()
                else:
                    data[formatted_key] = text[text.find(key)+len(key):].replace('\n', '').strip()
            # Return dictionary
            return data
    else:
        print(f'{pdf_file} - Invalid file format')


def check_pdf(pdf_file):
    if Path(pdf_file).suffix == '.pdf':
        pass


if __name__ == '__main__':
    print(read_pdf('test_task.pdf'))
    # check_pdf()
