import requests
from bs4 import BeautifulSoup
from dict_classes import classes
"""
获取url地址
"""

url_bis_gear = 'https://www.wowhead.com/cn/guide/classes/{worker}/{talent}/bis-gear#bis-items-mythic'

#动态链接url生成器
for key,value in classes.items():
    #print(f'{key}: {value}')
    for off in value:
        url = url_bis_gear.format(worker=key, talent=off)
        print(url)
