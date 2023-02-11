from check_pdf.model.object.pdf_processing import CheckPdf, CreateData
from itertools import zip_longest
import pytest
from check_pdf.model.data.pdf_data import PDFFileData


# @pytest.mark.parametrize(
#     "reference_file, checked_file, key_list",
#     [
#         (
#             "test_task.pdf", ['test_task.pdf'],
#             [
#                 'PN:', 'SN:', 'DESCRIPTION:', 'LOCATION:', 'CONDITION:', 'RECEIVER#:', 'UOM:', 'EXP DATE:', 'PO:',
#                 'CERT SOURCE:', 'REC.DATE:', 'MFG:', 'BATCH# :', 'DOM:', 'REMARK:', 'LOT# :', 'TAGGED BY:', 'Qty:',
#                 'NOTES:'
#             ]
#         )
#     ]
# )
# def test_check_pdf(reference_file, checked_file, key_list):
#     reference_file = CreateData().create_reference_file_data(reference_file, key_list)
#     checked_file = PDFFileData(checked_file, key_list)
#     cp = CheckPdf().read_pdf(reference_file)
#     cp1 = CheckPdf().read_pdf(checked_file)
#     assert cp1.keys() == cp.keys(), 'presence of elements does not match'
#     for i, k in zip_longest(cp, cp1):
#         assert i == k, 'file structure does not match'
