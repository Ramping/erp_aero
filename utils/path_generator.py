import os


def resources_path():
    return os.path.join(os.path.abspath('check_pdf'), 'resources')


def main_file_path(file_name: str):
    return os.path.join(os.path.join(resources_path(), 'main_file'), file_name)


def checked_files_path():
    return os.path.join(resources_path(), 'need_check')


def checked_file(file_name):
    return os.path.join(checked_files_path(), file_name)

