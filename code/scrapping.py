import requests
from bs4 import BeautifulSoup
import json

data = {}
data['anime'] = []

webpage = 'https://myanimelist.net/anime/season/schedule'

page = requests.get(webpage)

soup = BeautifulSoup(page.content, 'html.parser')

weekdays = [
    'js-seasonal-anime-list-key-monday', 'js-seasonal-anime-list-key-tuesday',
    'js-seasonal-anime-list-key-wednesday',
    'js-seasonal-anime-list-key-thursday', 'js-seasonal-anime-list-key-friday',
    'js-seasonal-anime-list-key-saturday', 'js-seasonal-anime-list-key-sunday'
]
i = 1
for day in weekdays:
    name_box = soup.findAll('div', attrs={'class': day})
    dayInfo = name_box[0].find('div', attrs={'class': 'anime-header'})
    for value in name_box:
        allNames = value.findAll('div', attrs={'class': 'seasonal-anime'})
        for name in allNames:
            title_tag = name.find('a', attrs={'class': 'link-title'})
            producer = name.find('span', attrs={'class': 'producer'})
            episodes = name.find('div', attrs={'class': 'eps'})
            airTime = name.find('span', attrs={'class': 'remain-time'})
            rating = name.find('span', attrs={'class': 'score'})
            image = name.find('img')
            description = name.find('span', attrs={'class': 'preline'})
            try:
                data['anime'].append({
                    'id':
                    i,
                    'title':
                    title_tag.text.replace('\n', '').strip(),
                    'producer':
                    producer.text.replace('\n', '').strip(),
                    'episodes':
                    episodes.text.replace('\n', '').strip(),
                    'airTime':
                    airTime.text.replace('\n', '').strip(),
                    'rating':
                    rating.text.replace('\n', '').strip(),
                    'weekday':
                    dayInfo.text.replace('\n', '').strip(),
                    "image":
                    image['src'],
                    'description':
                    description.text.replace('\n', '').strip(),
                })

                i += 1
            except:
                data['anime'].append({
                    'id':
                    i,
                    'title':
                    title_tag.text.replace('\n', '').strip(),
                    'producer':
                    producer.text.replace('\n', '').strip(),
                    'episodes':
                    episodes.text.replace('\n', '').strip(),
                    'airTime':
                    airTime.text.replace('\n', '').strip(),
                    'rating':
                    rating.text.replace('\n', '').strip(),
                    'weekday':
                    dayInfo.text.replace('\n', '').strip(),
                    "image":
                    image['data-src'],
                    'description':
                    description.text.replace('\n', '').strip(),
                })

                pass

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
