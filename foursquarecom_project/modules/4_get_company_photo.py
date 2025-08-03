import requests
import json


# Заголовки запроса
headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8",
    "origin": "https://foursquare.com",
    "referer": "https://foursquare.com/",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}


# URL запроса
url = "https://api.foursquare.com/v2/venues/57d2eb6f498e9835421484d3/photos"

# Параметры запроса
params = {
    "locale": "en",
    "explicit-lang": "false",
    "v": "20241112",
    "id": "57d2eb6f498e9835421484d3",
    "limit": 60,
    "offset": 0,
    "wsid": "1QMDTMEJVXGE0PM5DIOILNQNCYE10E",
    "oauth_token": "N5GBTRV4SNAVROJLPWJ3LVRKXVSEA1WY05ODMUYFPYOL3F5J",
}


# Выполнение запроса
response = requests.get(url, headers=headers, params=params)

# Проверка статуса ответа
if response.status_code == 200:

    data = response.json()

    photo_list = []

    photo_data = data['response']['photos']['groups'][0]

    for photo in photo_data['items']:
        prefix = photo['prefix']
        suffix = photo['suffix']
        photo_url = prefix + '360x360' + suffix
        print(photo_url)

    photo_list.append(photo_url)
    # print(photo_list)


    # with open('foursquare_photo.json', 'w', encoding='utf-8') as file:
    #     json.dump(data, file, indent=4, ensure_ascii=False)


else:
    print(f"Ошибка {response.status_code}: {response.text}")
