import requests, os
from helper.utils import safe_filename

async def download_from_url(url):
    if not os.path.exists("downloads"):
        os.mkdir("downloads")
    name = safe_filename(url.split("/")[-1])
    path = "downloads/" + name
    open(path, "wb").write(requests.get(url).content)
    return path
