import requests
"""
爬区官方物品信息
给数据库导入数据
"""
# 通过itemID 查询物品信息
token = "KR7XkqIGxMZ4p0u04RpLBCcKPcZ1905uWg"

def api_search_itemID():
    url = "https://tw.api.blizzard.com/data/wow/item/219314"
    params = {
        "namespace": "static-tw",
        "locale": "zh_CN",
        "access_token": token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}, {response.text}")


def api_serach_inform():
    url = "https://tw.api.blizzard.com/data/wow/search/item"

    max_page = 10

    for page in range(1,max_page+1):
        params = {
            "namespace": "static-tw",
            "locale": "zh_CN",
            "access_token": token,
            "_page": page
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            print(f"Results Count: {len(data['results'])}")
            if data['results']:
                for item in data['results']:
                    if item['data']['required_level'] == 80:
                        print(item['data']['name']['zh_CN'])

        else:
            print(f"Error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    api_search_itemID()