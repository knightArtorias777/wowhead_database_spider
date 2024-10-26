import pandas as pd
from DrissionPage import WebPage,Chromium
from bs4 import BeautifulSoup
import re
#item 分成三类 武器 装备 饰品 制造业
"""
分类：来源 ｜ 装备种类
来源：地下城｜团本｜制造业
装备分类：武器｜装备｜饰品
装备都有的公共字： 名字｜装等｜物品类型｜需要等级｜绑定｜绿字｜价钱｜（美化）
武器特有：伤害｜单双手｜攻速｜基础属性｜耐久度
装备特有：（套装）｜护甲｜（美化）｜耐久度｜基础属性

为了给数据库传入
itemID|name|item level|Bind|Unique-Equipped|equip-info(Basic-Attributes)|
Green-effects|requires-level|Sell-Price
"""

# todo 数据进入数据库 增删改查
# input itemUrl eg.https://www.wowhead.com/guide/classes/death-knight/frost/bis-geard
# output database postgres context
# input:list
def url_input(lst):
    # 总流程 把url内部多所有有用信息都放到数据库中
    for i in lst:
        url = lst[i]
        #
        json = url_filter(url)
        #增删改查操作

# 简单提取信息变成
# todo:装备改成类 函数替代
def url_filter(url):
    page = WebPage()
    page.set.load_mode.eager()
    page.get(url)
    re_feature = r'item=$/'
    itemID = re.findall(re_feature,url)
    html_content = page.raw_data
    # itemID
    soup = BeautifulSoup(html_content, 'html.parser')
    target_div = soup.find(id="tt221145")
    item_name = target_div.select_one('.q4').get_text(strip=True) if target_div else ""
    #quality = target_div.select_one('span[style="color: #00ff00"]').get_text(strip=True) if target_div else ""
    item_level = target_div.select_one('span.q').get_text(strip=True).split("：")[1] if target_div else ""
    upgrade_info = target_div.select_one('span.q:nth-of-type(2)').get_text(strip=True) if target_div else ""
    binding = target_div.find(text='拾取后绑定').strip() if target_div else ""
    required_level = target_div.find(text=lambda text: text and '需要等级' in text).split()[-1] if target_div else ""
    # 获取装备效果
    effects = [effect.get_text(strip=True) for effect in target_div.select('span.q2')] if target_div else []

    # 获取售价
    sell_price = target_div.select_one('.whtt-sellprice').get_text(strip=True) if target_div else ""

    # 获取掉落来源和几率 todo增加鲁棒性 可以没有
#    dropped_by = target_div.select_one('.whtt-droppedby').get_text(strip=True) if target_div else ""
#    drop_chance = target_div.select_one('.whtt-dropchance').get_text(strip=True) if target_div else ""

    # 输出结果
    print("物品名称:", item_name)
    #print("品质:", quality)
    print("物品等级:", item_level)
    print("升级信息:", upgrade_info)
    print("绑定类型:", binding)
    print("需要等级:", required_level)
    print("装备效果:", effects)
    print("售价:", sell_price)
#    print("掉落来源:", dropped_by)
#    print("掉落几率:", drop_chance)


if __name__ == '__main__':
    url1 = "https://www.wowhead.com/cn/item=221145/%E6%B2%89%E8%88%B9%E8%80%85%E7%9A%84%E5%A4%A7%E9%94%A4?bonus=657:11143:5878:7981:10299"
    url = "https://www.wowhead.com/cn/item=220305/%E6%AC%A7%E7%BB%B4%E7%BA%B3%E5%85%8B%E6%96%AF%E7%9A%84%E5%AC%97%E5%8F%98%E4%B9%8B%E5%8D%B5?bonus=7981:11143:5878:10299"
    url_filter(url1)