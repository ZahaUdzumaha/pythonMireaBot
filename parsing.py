import io
import os
import json
import requests
from aiogram.types import InputFile
from bs4 import BeautifulSoup as bs
from PIL import Image


def country_parsing():
    json_list = list()

    r = requests.get("https://ru.wikipedia.org/wiki/Список_государств")
    soup = bs(r.text, "html.parser")
    rows = soup.select('#mw-content-text > div.mw-parser-output > table:nth-child(8) > tbody')[0].contents
    for row in rows:
        if row == '\n':
            continue
        soup = bs(str(row), "html.parser")
        columns = soup.select('td')

        if len(columns) == 0:
            continue
        url = str(columns[1].select('a')[0].select('img')[0]['src']).removeprefix("//").replace("50px", "500px")
        name = str(columns[2].select('a')[0].text.strip())

        json_list.append(name)
        get_image(url, name)
    create_json(json_list)


def get_json():
    if not os.path.exists("country_data.json"):
        return
    with open("country_data.json", "r") as read_file:
        return json.load(read_file)


def create_json(data):
    if os.path.exists("country_data.json"):
        return
    with open("country_data.json", "w") as write_file:
        json.dump(data, write_file)


def get_image(url, name):
    if os.path.exists("flags/" + str(name) + ".jpg"):
        return InputFile("flags/" + str(name) + ".jpg")

    resource = requests.get(url="https://" + url, stream=True,
                            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

    try:
        image = Image.open(io.BytesIO(resource.content)).convert('RGB')
    except IOError as e:
        print(e)
        return

    image.save("flags/" + str(name) + ".jpg", 'jpeg')
    return InputFile("flags/" + str(name) + ".jpg")