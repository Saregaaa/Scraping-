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

# Параметры запроса
params = {
    "locale": "en",
    "explicit-lang": "false",
    "v": "20241112",
    "m": "foursquare",
    "offset": 0,
    "limit": 50,
    "sort": "popular",
    "wsid": "1QMDTMEJVXGE0PM5DIOILNQNCYE10E",
    "oauth_token": "N5GBTRV4SNAVROJLPWJ3LVRKXVSEA1WY05ODMUYFPYOL3F5J",
}

# URL запроса
url = "https://api.foursquare.com/v2/venues/4be442b02457a593e9f3a915/tips"


response = requests.get(url, headers=headers, params=params)

comments_list = []

# Проверка ответа
if response.status_code == 200:
    
    data = response.json()

    comment_data = data['response']['tips']['items']

    for comment in comment_data:

        print('-' * 50)

        try:
            comment_text = comment['text']
            print("Comment: ", comment_text)
        except Exception as e:
            comment_text = None
            print("Comment: ", comment_text)

        try:
            coment_user_last_name = comment['user']['lastName']
            print("Last name: ", coment_user_last_name)
        except Exception as e:
            coment_user_last_name = None
            print("Last name: ", coment_user_last_name)

        try:
            comment_user_first_name = comment['user']['firstName']
            print('First name: ', comment_user_first_name)
        except Exception as e:
            comment_user_first_name = None
            print("First name: ", comment_user_first_name)

        try:
            comment_user_photo = comment['user']['photo']['prefix'] + '360x360' + comment['user']['photo']['suffix']
            print(comment_user_photo)
        except Exception as e:
            comment_user_photo = None
            print("Photo: ", comment_user_photo)

        comments_list.append(
            {
                'comment_text': comment_text,
                'comment_user_last_name': coment_user_last_name,
                'comment_user_first_name': comment_user_first_name,
                'comment_user_photo': comment_user_photo
            })


    print(comments_list)
    # with open('foursquare_comment.json', 'w', encoding='utf-8') as file:
    #     json.dump(data, file, indent=4, ensure_ascii=False)


else:
    print(f"Ошибка {response.status_code}: {response.text}")
