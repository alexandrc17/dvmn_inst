import requests
from load_photo import load_photo


def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v3/launches/latest", verify=False)
    response.raise_for_status()
    data = response.json()
    result = data['links']['flickr_images']
    for url_number, url in enumerate(result, 1):
        filename = 'img/spacex{}.jpg'.format(url_number)
        load_photo(url, filename)
