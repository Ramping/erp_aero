from check_pdf.model.controls.read_pdf import read_reference_pdf, read_check_pdf


class CreateFileStructure:

    @staticmethod
    def base_create(pdffiledata, keys):
        text = read_reference_pdf(pdffiledata)
        data = dict()
        for index, key in enumerate(keys):
            formatted_key = key.replace(':', '').strip()
            if index + 1 < len(keys):
                value = text[text.find(key) + len(key):text.find(keys[index + 1])]
                data[formatted_key] = value.replace('\n', '').strip()
            else:
                data[formatted_key] = text[text.find(key) + len(key):].replace('\n', '').strip()
        return data

    def create_main_structure(self, pdffiledata):
        # self.base_create(pdffiledata, pdffiledata.keys)
        text = read_reference_pdf(pdffiledata)
        data = dict()
        for index, key in enumerate(pdffiledata.keys):
            formatted_key = key.replace(':', '').strip()
            if index + 1 < len(pdffiledata.keys):
                value = text[text.find(key) + len(key):text.find(pdffiledata.keys[index + 1])]
                data[formatted_key] = value.replace('\n', '').strip()
            else:
                data[formatted_key] = text[text.find(key) + len(key):].replace('\n', '').strip()
        return data

    @staticmethod
    def create_checked_file_structure(pdffiledata):
        for i in pdffiledata.checked_file:

            text = read_check_pdf(i)
            data = dict()
            for index, key in enumerate(pdffiledata.keys):
                formatted_key = key.replace(':', '').strip()
                if index + 1 < len(pdffiledata.keys):
                    value = text[text.find(key) + len(key):text.find(pdffiledata.keys[index + 1])]
                    data[formatted_key] = value.replace('\n', '').strip()
                else:
                    data[formatted_key] = text[text.find(key) + len(key):].replace('\n', '').strip()
            return data
