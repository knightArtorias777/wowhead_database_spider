import json
import pandas as pd
from DrissionPage import WebPage,Chromium
import re

"""
分类：来源 ｜ 装备种类
来源：地下城｜团本｜制造业
装备分类：武器｜装备｜饰品
装备都有的公共字： 名字｜装等｜物品类型｜需要等级｜绑定｜绿字｜价钱｜（美化）
武器特有：伤害｜单双手｜攻速｜基础属性｜耐久度
装备特有：（套装）｜护甲｜（美化）｜耐久度｜基础属性
df 乱数据
    名字 品质 物品等级 升级 绑定 唯一 装备位置 属性 


为了给数据库传入
itemID|name|item level|Bind|Unique-Equipped|equip-info(Basic-Attributes)|
Green-effects|requires-level|Sell-Price
"""

# todo 数据进入数据库 增删改查
# input itemUrl eg.https://www.wowhead.com/guide/classes/death-knight/frost/bis-geard
# output database postgres context
# input:list
def parse_item_description(description):
    # 定义正则表达式模式
    patterns = {
        '名字': r'^(.*?)\n',
        '唯一': r'(装备唯一)',
        '位置': r'(饰品|单手.*?权杖|胸部.*?板甲.*?护甲)',
        '属性': r'(\+\d+ .*?)\n',  # 匹配所有加成属性
        '套装效果': r'\((\d+) 组合 .*\): (.*?)(?=\n\(|$)',  # 匹配套装效果
        '职业': r'职业：(.*?)\n',
        '掉落于': r'掉落于: (.*?)\n',
        '掉落几率': r'掉落几率: (\d+\.\d+)%'
    }
    effect_use_cooldown_pattern = r"""
        装备：\s*(.*?)(?:\n使用:|$)  # 效果部分
        (?:\n使用: (.*?))?           # 使用部分（可选）
        (?:\n\((.*?) 冷却\))?        # 冷却部分（可选）
        """
    effect_use_cooldown_match = re.search(effect_use_cooldown_pattern, description, re.DOTALL | re.VERBOSE)
    item_data = {}
    for key, pattern in patterns.items():
        if key == '属性':
            # 对于属性，我们需要找到所有的匹配项
            matches = re.findall(pattern, description)
            if matches:
                item_data[key] = matches
            else:
                item_data[key] = []
        elif key == '套装效果':
            # 对于套装效果，我们需要找到所有的匹配项
            matches = re.findall(pattern, description, re.DOTALL)
            if matches:
                item_data[key] = {int(match[0]): match[1].strip() for match in matches}
            else:
                item_data[key] = {}
        else:
            match = re.search(pattern, description, re.DOTALL)
            if match:
                item_data[key] = match.group(1).strip() if len(match.groups()) > 0 else match.group(0).strip()
            else:
                item_data[key] = None
    if effect_use_cooldown_match:
        item_data['效果'] = effect_use_cooldown_match.group(1).strip() if effect_use_cooldown_match.group(1) else None
        item_data['使用'] = effect_use_cooldown_match.group(2).strip() if effect_use_cooldown_match.group(2) else None
        item_data['冷却'] = effect_use_cooldown_match.group(3).strip() if effect_use_cooldown_match.group(3) else None
    else:
        item_data['效果'] = None
        item_data['使用'] = None
        item_data['冷却'] = None

    return item_data

def url_input(lst):
    # 总流程 把url内部多所有有用信息都放到数据库中
    return
def texts_handle(list):
    if list is None:
        return "error"
    l1:str = list[0]
    noyet_data =l1.split("\n")
    json_str =json.dumps(noyet_data,ensure_ascii=False, indent=4)
    print(json_str)

# 简单提取信息变成
# todo:装备改成类 函数替代
def url_filter(url):
    #open a website
    page = WebPage()
    page.set.load_mode.eager()
    page.get(url)
    # obtain itemid:list by re
    re_feature = r'(?<=item=)\d+'
    itemid = re.findall(re_feature,url)

    print(itemid)
    e = page.ele(f"@id=tt{itemid[0]}").text
    print(e)
    #print(parse_item_description(e))



if __name__ == '__main__':
    url1 = "https://www.wowhead.com/cn/item=221145/%E6%B2%89%E8%88%B9%E8%80%85%E7%9A%84%E5%A4%A7%E9%94%A4?bonus=657:11143:5878:7981:10299"
    url = "https://www.wowhead.com/cn/item=220305/%E6%AC%A7%E7%BB%B4%E7%BA%B3%E5%85%8B%E6%96%AF%E7%9A%84%E5%AC%97%E5%8F%98%E4%B9%8B%E5%8D%B5?bonus=7981:11143:5878:10299"
    urln = 'https://www.wowhead.com/item=222451/charged-slicer?bonus=10222:1515:8960:11300:8791'
    url2 ='https://www.wowhead.com/cn/item=212005/%E5%87%BA%E5%9C%9F%E7%9A%84%E7%99%BE%E5%A4%AB%E9%95%BF%E8%83%B8%E9%93%A0?bonus=7981:11143:5878:10299'
    url_filter(url)
    #url_filter(url1)
    #url_filter(url2)