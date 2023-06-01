import os


class FileManager:
    def create_file(self, file_path):
        with open(file_path, 'w') as file:
            pass

    def append_to_file(self, file_path, content):
        with open(file_path, 'a') as file:
            file.write(content)
