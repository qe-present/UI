import csv

import requests
import re

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9278'
r = requests.get(url=url)
station_name = re.findall('var station_names =\'(.*)\'', r.text)[0]
station_list = station_name.split('@')

with open("station.csv", "a", encoding="utf-8", newline="") as f:
    writer=csv.writer(f)
    writer.writerow(['cdoe','name'])
    for i in station_list:
        if i == '':
            continue
        place_list=i.split('|')
        place_name = place_list[1]
        place_code=place_list[2]
        writer.writerow([place_code,place_name])

