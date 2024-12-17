import os


def open_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def write_file(content, file_path):
    with open(file_path, 'w') as file:
        file.write(content)

