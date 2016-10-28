import requests
from bs4 import BeautifulSoup

class Film:
    def __init__(self, name, description, rating):
        self.name = name
        self.description = description
        self.rating = rating


html = requests.get('https://kinoafisha.ua/kinoafisha/').text
parsed_html_document = BeautifulSoup(html, "lxml")

films = parsed_html_document.find_all('h3')
films = [film.text for film in films]

descriptions = parsed_html_document.find_all('div', class_="countries")
descriptions = [desc.text.replace("\r\n", '').strip() for desc in descriptions]

ratings = parsed_html_document.find_all('div', class_='rating')
ratings = [result.text.split('\r\n')[1].strip() for result in ratings]

my_films = [Film(films[i], descriptions[i], ratings[i]) for i in range(len(films))]

pass
