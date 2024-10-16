from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup("<html>data</html>")

df_url = 'https://www.wowhead.com/cn/guide/mythic-plus-dungeons/the-war-within-season-1/loot'
raid_url= 'https://www.wowhead.com/cn/items/min-req-level:80/max-req-level:80/group-by:slot?filter=128:195;4:1;0:0#slot-2'
