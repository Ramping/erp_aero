from voluptuous import Schema

from check_pdf.model.controls.creating_file_structure import CreateFileStructure


class CheckPdf:

    def __init__(self):
        self.schema = Schema(
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

    def read_pdf(self, pdffiledata):
        return CreateFileStructure().create_main_structure(pdffiledata)

    def presence_elements(self):
        assert cp1.keys() == cp.keys()

    def conformity_structure(self):
        for i, k in zip_longest(cp, cp1):
            assert i == k


class TmpClass:

    def tmpfunc(self, reference_file):
        return CheckPdf().read_pdf(reference_file)

    def read_pdf(self, pdffiledata):
        return CreateFileStructure().create_checked_file_structure(pdffiledata)
