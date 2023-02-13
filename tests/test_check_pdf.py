import allure
import pytest
from check_pdf.model.data.pdf_data import PDFFileData
from check_pdf.model.object.pdf_processing import CheckPdf


class TestPDFFiles:
    @pytest.mark.all_tests
    @pytest.mark.pdf_test
    @allure.tag('PDF')
    @allure.label('owner', 'aapopov')
    @allure.feature('Checking pdf files')
    @allure.story('''Develop a method that accepts a PDF file as input. 
                    It is necessary to read all possible information from the file and return it as a dictionary at the output.
                    Using this file as a reference, develop a mechanism that checks incoming pdf files for the presence of all elements and structure compliance.''')
    @pytest.mark.parametrize('reference_file_name, data', [('test_task_main.pdf', [
        'PN:', 'SN:', 'DESCRIPTION:', 'LOCATION:', 'CONDITION:', 'RECEIVER#:', 'UOM:', 'EXP DATE:', 'PO:',
        'CERT SOURCE:', 'REC.DATE:', 'MFG:', 'BATCH# :', 'DOM:', 'REMARK:', 'LOT# :', 'TAGGED BY:', 'Qty:',
        'NOTES:'
    ])])
    def test_task_pdf(self, reference_file_name, data):
        reference_file = PDFFileData(reference_file=reference_file_name, keys=data)
        task_file = CheckPdf()
        with allure.step('schema validation'):
            assert task_file.assertion_schema(reference_file)
        with allure.step('checking for the presence of elements (optional)'):
            assert task_file.assertion_presence_of_elements(reference_file)
