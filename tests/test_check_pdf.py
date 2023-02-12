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
    @allure.story('''Разработать метод, на вход которого подается PDF файл (сам файл предоставляется во вложении). 
                    Нужно прочитать всю возможную информацию из файла и на выходе вернуть в виде словаря.
                    Используя этот файл как эталон, разработать механизм, проверяющий входящие pdf-файлы на наличие
                     всех элементов и соответствие структуры (расположение на листе). ''')
    @pytest.mark.parametrize('reference_file_name, data', [('test_task.pdf', [
        'PN:', 'SN:', 'DESCRIPTION:', 'LOCATION:', 'CONDITION:', 'RECEIVER#:', 'UOM:', 'EXP DATE:', 'PO:',
        'CERT SOURCE:', 'REC.DATE:', 'MFG:', 'BATCH# :', 'DOM:', 'REMARK:', 'LOT# :', 'TAGGED BY:', 'Qty:',
        'NOTES:'
    ])])
    def test_task_pdf(self, reference_file_name, data):
        reference_file = PDFFileData(reference_file=reference_file_name, keys=data)
        task_file = CheckPdf()
        with allure.step(''):
            assert task_file.assertion_schema(reference_file)
        with allure.step(''):
            assert task_file.assertion_presence_of_elements(reference_file)
