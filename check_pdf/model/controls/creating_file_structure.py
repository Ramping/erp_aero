from check_pdf.model.controls.read_pdf import read_reference_pdf, read_check_pdf


class CreateFileStructure:

    @staticmethod
    def create_main_structure(pdffiledata):
        try:
            text = read_reference_pdf(pdffiledata)
            data = dict()
            for index, key in enumerate(pdffiledata.keys):
                formatted_key = key.replace(':', '').strip()
                if index + 1 < len(pdffiledata.keys):
                    value = text[text.find(key) + len(key):text.find(pdffiledata.keys[index + 1])]
                    data[formatted_key] = value.replace('\n', '').replace(':', '').strip()
                else:
                    data[formatted_key] = text[text.find(key) + len(key):].replace('\n', '').replace(':', '').strip()
            return data
        except:
            raise ValueError('invalid file format or content')

    @staticmethod
    def create_checked_file_structure(file_name, keys):
        try:
            text = read_check_pdf(file_name)
            data = dict()
            for index, key in enumerate(list(keys.keys())):
                formatted_key = key.replace(':', '').strip()
                if index + 1 < len(list(keys.keys())):
                    value = text[text.find(key) + len(key):text.find(list(keys.keys())[index + 1])]
                    data[formatted_key] = value.replace('\n', '').replace(':', '').strip()
                else:
                    data[formatted_key] = text[text.find(key) + len(key):].replace('\n', '').replace(':', '').strip()
            return data
        except:
            raise ValueError('invalid file format or content')

