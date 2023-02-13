import os
from pytest_voluptuous import S
from utils.path_generator import checked_files_path as cfp
from voluptuous import Schema
from check_pdf.model.controls.creating_file_structure import CreateFileStructure


class CheckPdf:

    def __init__(self):
        self.cms = CreateFileStructure()
        self._schema = Schema(
            {
                'PN': str,
                'SN': str,
                'DESCRIPTION': str,
                'LOCATION': str,
                'CONDITION': str,
                'RECEIVER#': str,
                'UOM': str,
                'EXP DATE': str,
                'PO': str,
                'CERT SOURCE': str,
                'REC.DATE': str,
                'MFG': str,
                'BATCH#': str,
                'DOM': str,
                'REMARK': str,
                'LOT#': str,
                'TAGGED BY': str,
                'Qty': str,
                'NOTES': str
            }
        )

    def _main_structure(self, pdffiledata):
        return self.cms.create_main_structure(pdffiledata)

    def _checked_structure(self, pdffiledata, file_name):
        return self.cms.create_checked_file_structure(file_name, self.cms.create_main_structure(pdffiledata))

    def assertion_schema(self, pdffiledata):
        checking_files_list = os.listdir(cfp())
        if len(checking_files_list) > 0:
            for file_name in checking_files_list:
                assert S(self._schema) == self._checked_structure(pdffiledata, file_name)
        else:
            raise FileNotFoundError('files to be checked are missing in the resources/need_check directory')
        return self

    def assertion_presence_of_elements(self, pdffiledata):
        checking_files_list = os.listdir(cfp())
        if len(checking_files_list) > 0:
            for file_name in checking_files_list:
                assert list(self._checked_structure(pdffiledata, file_name).keys()) == list(self._main_structure(pdffiledata).keys())
        else:
            raise FileNotFoundError('files to be checked are missing in the resources/need_check directory')
        return self

