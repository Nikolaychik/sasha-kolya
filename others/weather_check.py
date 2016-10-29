import requests
from bs4 import BeautifulSoup


class WeatherCollector:
    def __init__(self):
        html = requests.get('https://ua.sinoptik.ua/погода-київ').text
        self.parsed_html_document = BeautifulSoup(html, 'lxml')

    def sinoptik_current_temperature_kiev(self):
        current_temp = self.parsed_html_document.find('p', class_='today-temp').text
        return current_temp

    def sinoptik_min_temperature_current_day_kiev(self):
        today_min = self.parsed_html_document.find('div', class_='min').text[-3:]
        return today_min

    def sinoptik_max_temperature_current_day_kiev(self):
        max_temp = self.parsed_html_document.find('div', class_='max').text[-3:]
        return max_temp

    def sinoptik_min_temperature_kiev_historyval(self):
        current_temp = self.parsed_html_document.find('p', class_='infoHistoryval').text.split(':')[2][1:7]
        return current_temp

    def sinoptik_max_temperature_kiev_historyval(self):
        current_temp = self.parsed_html_document.find('p', class_='infoHistoryval').text.split(':')[1][1:6]
        return current_temp

    def sinoptik_info_day_light_down_time(self):
        day_light_down_time = \
        str(self.parsed_html_document.find('div', class_='infoDaylight').text).strip().split('Захід ')[1]
        return day_light_down_time
