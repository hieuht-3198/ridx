import zipfile

def unzip_file(path_to, extract_to):
  with zipfile.ZipFile(path_to, 'r') as zip_ref:
      zip_ref.extractall(extract_to)