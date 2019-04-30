import requests
from bs4 import BeautifulSoup

webpage = 'https://myanimelist.net/anime/season/schedule'

page = requests.get(webpage)

soup = BeautifulSoup(page.content, 'html.parser')

weekdays = [
    'js-seasonal-anime-list-key-monday', 'js-seasonal-anime-list-key-tuesday',
    'js-seasonal-anime-list-key-wednesday',
    'js-seasonal-anime-list-key-thursday', 'js-seasonal-anime-list-key-friday',
    'js-seasonal-anime-list-key-saturday', 'js-seasonal-anime-list-key-sunday'
]

for day in weekdays:
    name_box = soup.findAll('div', attrs={'class': day})
    for value in name_box:
        allNames = value.findAll('div', attrs={'class': 'seasonal-anime'})
        for name in allNames:
            title_tag = name.find('a', attrs={'class': 'link-title'})
            producer = name.find('span', attrs={'class': 'producer'})
            episodes = name.find('div', attrs={'class': 'eps'})
            airTime = name.find('span', attrs={'class': 'remain-time'})
            print(title_tag.text, airTime.text)
