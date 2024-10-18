from DrissionPage import Chromium
"""
爬取wowhead raid mythic bis数据
"""

#spider web address
df_url = 'https://www.wowhead.com/cn/guide/mythic-plus-dungeons/the-war-within-season-1/loot'
raid_url= 'https://www.wowhead.com/cn/items/min-req-level:80/max-req-level:80/group-by:slot?filter=128:195;4:1;0:0#slot-2'
test_url='https://www.wowhead.com/cn/guide/classes/Death-Knight/Unholy/bis-gear#bis-items-raid'

#list[0]information list[2]equid table
def bis_url_spider(url)->list:
    tab = Chromium().latest_tab
    tab.get(test_url)
    raid = tab.ele('@@tag()=div@@id=tab-bis-items-mythic')
    return raid.texts()


#
# def spider_df(df_url):
#     response = driver.get(df_url)
#     if response.status_code == 200:
#         print(response.text)
#         # 启用分析器
#         #soup = BeautifulSoup(response.text, 'lxml')
#         # 对div id='tab-bis-items-raid'和 div id ='tab-bis-items-mythic'内部爬虫
#         #print(soup)
#
#     else:
#         print(f"error response{response.status_code}")

# 函数是在做 通过url 从详细页面信息获取
def get_tb_url (url):
    return

if "__main__" == __name__:
    print(bis_url_spider(test_url))