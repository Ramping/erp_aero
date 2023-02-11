import os


# def resources_path():
#     return os.path.join(
#         os.path.join(
#             os.path.abspath(
#                 os.path.join(os.getcwd(), os.path.pardir)
#             ), 'check_pdf'
#         ), 'resources'
#     )

def resources_path():
    return os.path.join(os.path.abspath('check_pdf'), 'resources')


def main_file_path(file_name: str):
    return os.path.join(os.path.join(resources_path(), 'main_file'), file_name)


def checked_files():
    return os.path.abspath(os.path.join(resources_path(), 'need_check'))


def list_checked_files():
    return os.listdir(os.path.abspath(os.path.join(resources_path(), 'need_check')))
