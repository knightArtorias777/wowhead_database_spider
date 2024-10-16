import requests
"""
还想着用官方API 
物品信息调用可以倒是
"""
url = "https://tw.api.blizzard.com/data/wow/search/item"
token = "KRRF3u5X6YUFbUwy9lMCoePthKK4GcOp1C"
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
