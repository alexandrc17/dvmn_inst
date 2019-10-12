import requests
import os
from PIL import Image
from instabot import Bot
from fetch_hubble import fetch_collection
from fetch_spacex import fetch_spacex_last_launch


def resize_img(path): #ex.: "img/"
    list_img = os.listdir(path)
    for img in list_img:
        image = Image.open(path+img)
        if image.width > image.height:
            coordinates = (image.width - image.height, 0, image.size[0], image.size[1])
        else:
            coordinates = (0, image.height - image.width, image.size[0], image.size[1])
        cropped = image.crop(coordinates)
        cropped.save(path + img)


def upload_inst(path_image):
    bot = Bot()
    bot.login()
    fetch_collection('wallpaper')
    fetch_spacex_last_launch()
    resize_img("img/")
    list_img = os.listdir(path_image)
    for img in list_img:
        try:
            bot.upload_photo(path_image+img, caption="Elon Mask")
        except RuntimeError:
            continue


if __name__ is '__main__':
    upload_inst()
