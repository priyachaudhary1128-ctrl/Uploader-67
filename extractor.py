import zipfile, os

def extract_zip(path):
    out = path + "_unzipped/"
    os.makedirs(out, exist_ok=True)
    with zipfile.ZipFile(path, 'r') as z:
        z.extractall(out)
    return out
