from bs4 import Tag
from lxml.doctestcompare import strip


def div_convert(itemid:int,target: Tag):
    # itemid ˚∆˚
    item_id = itemid
    # name
    item_name = target.select_one(".q4").get_text(strip=True) if target else ""
    # epic
#    item_quality = target.select_one('span[style="color:#00ff00"]').get_text(strip=True) if target else ""
    # item level
    q= [rank.get_text(strip=True) for rank in target.select_one('span.q')] if target else []
    # weapon class 考虑要素很多 考虑用注释进行检索
    q1= [info.get_text(strip=True) for info in target.select_one('span.q1')] if target else []
    # green font 很多 用list收集 √
    green_font = [effect.get_text(strip=True) for effect in target.select('span.q2')] if target else []

    #     # 输出结果
    print("物品序列:",item_id)
    print("物品名称:", item_name)
#   print("品质:", item_quality)
    print("物品等级:", q)
    print("物品信息:", q1)
    #     print("升级信息:", upgrade_info)
    #     print("绑定类型:", binding)
    #     print("需要等级:", required_level)
    print("装备效果:", green_font)

class equipinfo:
    itemID: int
    def __init__(self, itemID):
        self.itemID = itemID


    #todo 属性
    """
    itemID|name|item level|Bind|Unique-Equipped|equip-info(Basic-Attributes)|
    Green-effects|requires-level|Sell-Price
    """
    # input:div_target
    # output: 集很多信息的class
    @staticmethod
    def div_convert(target:Tag):
        #itemid
        # name
        item_name = target.select_one(".q4").get_text(strip=True) if target else ""
        # epic
        quality = target.select_one('span[style="color:#00ff00"]').get_text(strip=True) if target else ""
        #item level
        item_level =target.select_one('span.q').get_text(strip=True) if target else ""
        #weapon class 考虑要素很多 考虑用注释进行检索
        info =target.select_one('span.q1').get_text(strip=True) if target else ""
        #green font 很多 用list收集
        green_font = [effect.get_text(strip=True) for effect in target.select('span.q2')] if target else []

        #     # 输出结果
        print("物品名称:", item_name)
        print("品质:", quality)
        print("物品等级:", item_level)
        print("物品信息:",info)

        print("装备效果:", green_font)


