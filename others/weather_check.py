import requests
from bs4 import BeautifulSoup


def sinoptik_temperature_current_kiev():
    html = requests.get('https://ua.sinoptik.ua/погода-київ').text
    parsed_html_document = BeautifulSoup(markup=html)
    current_temp = parsed_html_document.find('p', class_='today-temp').text
    return current_temp
