import requests
from datetime import datetime
from bs4 import BeautifulSoup

def show_definitions(soup):
    senseList = []
    senses = soup.find_all('li', class_='sense')
    for s in senses:
        definition = s.find('span', class_='def').text
        print(definition)

word_to_search = 'warp'
scrape_url = 'https://www.oxfordlearnersdictionaries.com/definition/english/' + word_to_search

headers = {"User-Agent": ""}
web_response = requests.get(scrape_url, headers=headers)

if web_response.status_code == 200:
    soup = BeautifulSoup(web_response.text, 'html.parser')

    try:
        show_definitions(soup)
    except AttributeError:
        print('Word not found!!')
else:
    print('Failed to get response...')