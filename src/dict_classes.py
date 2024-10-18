"""职业对应天赋的字典"""
# url中会用到
classes = {
    'Death-Knight':{
        'Blood',
        'Frost',
        'Unholy'
    },
    # 'Demon Hunter': {
    #     'Arcane': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Fire': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Frost': {'Role': 'DPS', 'Primary Stat': 'Intellect'}
    # },
    # 'Evoker': {
    #     'Arcane': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Fire': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Frost': {'Role': 'DPS', 'Primary Stat': 'Intellect'}
    # },
    # 'Hunter': {
    #     'Arcane': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Fire': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Frost': {'Role': 'DPS', 'Primary Stat': 'Intellect'}
    # },
    # 'Mage': {
    #     'Arcane': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Fire': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Frost': {'Role': 'DPS', 'Primary Stat': 'Intellect'}
    # },
    # 'Monk': {
    #     'Arcane': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Fire': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Frost': {'Role': 'DPS', 'Primary Stat': 'Intellect'}
    # },
    # 'Paladin': {
    #     'Arcane': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Fire': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Frost': {'Role': 'DPS', 'Primary Stat': 'Intellect'}
    # },
    # 'Priest': {
    #     'Arcane': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Fire': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Frost': {'Role': 'DPS', 'Primary Stat': 'Intellect'}
    # },
    # 'Rogue': {
    #     'Arcane': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Fire': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Frost': {'Role': 'DPS', 'Primary Stat': 'Intellect'}
    # },
    # 'Shaman': {
    #     'Arcane': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Fire': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Frost': {'Role': 'DPS', 'Primary Stat': 'Intellect'}
    # },
    #
    # 'Warlock': {
    #     'Arcane': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Fire': {'Role': 'DPS', 'Primary Stat': 'Intellect'},
    #     'Frost': {'Role': 'DPS', 'Primary Stat': 'Intellect'}
    # },
    # 'Warrior': {
    #     'Arms': {'Role': 'DPS', 'Primary Stat': 'Strength'},
    #     'Fury': {'Role': 'DPS', 'Primary Stat': 'Strength'},
    #     'Protection': {'Role': 'Tank', 'Primary Stat': 'Strength'}
    # }
}


class profession():
    def  __init__(self):
        name = self.name
