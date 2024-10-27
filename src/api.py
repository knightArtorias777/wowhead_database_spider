import urllib.parse
import json
import requests
import pandas as pd
"""
爬区官方物品信息
给数据库导入数据
"""
# 通过itemID 查询物品信息
#curl -u 58d28956d6324816a192760cde31e3ba:wuas5YhnGRZFkDkt66h7kv4I5vZTPOW8
# -d grant_type=client_credentials https://oauth.battle.net/token


def api_search_itemID():
    token = "KRqVTSIfMVcTNno94QfN7wdhMaGd7WH0YZ"
    base_url = "https://tw.api.blizzard.com/data/wow/item/221023"

    params = {
        "namespace": "static-tw",
        "locale": "zh_CN",
        "access_token": token
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")


if __name__ == '__main__':
    api_search_itemID()