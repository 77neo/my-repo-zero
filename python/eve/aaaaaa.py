import requests
from datetime import datetime
from bs4 import BeautifulSoup


def show_definitions(soup):
    print()
    senseList = []
    senses = soup.find_all('li', class_='sense')
    for s in senses:
        definition = s.find('span', class_='def').text
        print("-", definition)

        # Examples
        examples = s.find_all('ul', class_='examples')
        for e in examples:
            for ex in e.find_all('li'):
                print('\t-', ex.text)


word_to_search = 'glass+onion+launch+date+netf  lix'
scrape_url = 'https://www.google.com/search?q=' + word_to_search

headers = {"User-Agent": ""}
web_response = requests.get(scrape_url, headers=headers)
if web_response.status_code == 200:
    soup = BeautifulSoup(web_response.text, 'html.parser')
    print(soup.find('div', class_='BNeawe s3v9rd AP7Wnd').text)

else:
    print('Failed to get response...')