import zipfile
import os


def unzip_if_needed(path):
    filename, file_extension = os.path.splitext(path)
    if file_extension == ".zip":
        zip_ref = zipfile.ZipFile(path, 'r')
        zip_ref.extractall("credentials_temp")
        zip_ref.close()
        path = "credentials_temp/credentials.json"
    return path
