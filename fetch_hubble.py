import requests
from load_photo import load_photo


def img_ext(path):
    return path.split('.')[-1]


def download_img_hubble(id):
    response = requests.get("http://hubblesite.org/api/v3/image/{}".format(id), verify=False)
    response.raise_for_status()
    data = response.json()['image_files']
    url = []
    for url_image in data:
        url_image = url_image['file_url']
        url.append(url_image)
    url = "http:"+url[-1]
    filename = 'img/image_{}.{}'.format(id, img_ext(url))
    load_photo(url, filename)


def fetch_collection(collection):
    response = requests.get("http://hubblesite.org/api/v3/images?collection_name={}".format(collection), verify=False)
    response.raise_for_status()
    data = response.json()
    for id in data:
        id = id['id']
        download_img_hubble(id)
        print("ok")