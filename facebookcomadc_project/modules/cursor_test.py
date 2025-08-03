from load_django import *
from parser_app.models import *
import requests
import json
import datetime
from time import sleep

# URL for the POST request
url = "https://www.facebook.com/api/graphql/"

# Full headers
headers = {
    "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.facebook.com",
    "pragma": "no-cache",
    "referer": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&media_type=all&q=brianna&search_type=keyword_unordered",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-full-version-list": '"Google Chrome";v="131.0.6778.69", "Chromium";v="131.0.6778.69", "Not_A Brand";v="24.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Linux"',
    "sec-ch-ua-platform-version": '"6.8.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-asbd-id": "129477",
    "x-fb-friendly-name": "AdLibrarySearchPaginationQuery",
    "x-fb-lsd": "5sy4PbExRZsXwUb0_0jDuo",
}

# Full cookies
cookies = {
    "datr": "6YNNZjcT22BX_q1cmcvweHuo",
    "sb": "QfJOZgvom_J8GZWy-d9wAG4i",
    "c_user": "100016622866824",
    "ps_l": "1",
    "ps_n": "1",
    "dpr": "2",
    "ar_debug": "1",
    "fr": "19UzrKMxQNf4MbWmc.AWWVEg0J3nHUF1FnDxdi4xUmtXA.BnQtBU..AAA.0.0.BnQtBU.AWVRgSUzjo4",
    "xs": "48%3AVkgIFX0bWNgFSA%3A2%3A1719554535%3A-1%3A16378%3A%3AAcVRB7vNRq6_n0RaSDyRrp0j7R1D9ugW82HkEW_HCmo",
    "wd": "1850x498",
}

# Full payload
payload = {
    "av": "100016622866824",
    "__aaid": "0",
    "__user": "100016622866824",
    "__a": "1",
    "__req": "11",
    "__hs": "20051.HYP:comet_plat_default_pkg.2.1..2.1",
    "dpr": "2",
    "__ccg": "MODERATE",
    "__rev": "1018452212",
    "__s": "s16wj6:e46s1g:9xzj6p",
    "__hsi": "7440738787576568825",
    "__dyn": "7xeUmxa13yoS1syUbFp432m2q1Dxu13wqovzEdF8ixy360CEbo9E3-xS6Ehw2nVEK12wvk0ie2O1VwBwXwEwgo9oO0iS12x62G3i1ywOwv89k2C1FwaG5E6i588Egz898mwkE-U6-3e4UaEW0KrK2S1qxaawse5o4q0HUkw4BwMzUdEGdwzwea0K-1Lwqp8aE2cwAwQwr86C0nC1TwmUaE2Tw",
    "__csr": "isy949aFeCjJRy8KnzQHhpbHKUHOaG9VaCnLyoiye484eU6e1rxC3W2y0Lo1883ewYw9e04tE00Hfq1Mw",
    "__comet_req": "1",
    "fb_dtsg": "NAcP05RRMNny7GXpdoWG75cJtB-EA5e0zyq9i3jLifOGcYO1ttiEW_A:48:1719554535",
    "jazoest": "25338",
    "lsd": "5sy4PbExRZsXwUb0_0jDuo",
    "__spin_r": "1018452212",
    "__spin_b": "trunk",
    "__spin_t": "1732432001",
    "__jssesw": "1",
    "fb_api_caller_class": "RelayModern",
    "fb_api_req_friendly_name": "AdLibrarySearchPaginationQuery",
    "variables": json.dumps({
            "activeStatus":"active",
            "adType":"ALL",
            "bylines":[],
            "collationToken":"064e40b2-a8de-41e8-956b-e60fc221fcc1",
            "contentLanguages":[],
            "countries":["US"],
            "cursor":"AQHRFCH3aNcESm4VDx4GmcQeU8sRy5-4ATDDwQ7TFU2fCp6GouHMQkpPOF7JbprmIGJ8",
            "excludedIDs":None,
            "first":30,
            "location":None,
            "mediaType":"all",
            "pageIDs":[],
            "potentialReachInput":None,
            "publisherPlatforms":[],
            "queryString":"ads",
            "regions":None,
            "searchType":"keyword_unordered",
            "sessionID":"400a5cf0-44ee-4158-93f6-b120b1de3aac",
            "sortData":None,
            "source":None,
            "startDate":None,
            "v":"ac8592",
            "viewAllPageID":"0"
        }),
    "server_timestamps": "true",
    "doc_id": "27545919331688429",
}

# Make the POST request
# response = requests.post(url, headers=headers, cookies=cookies, data=payload)

seen_cursors = set()  # Для отслеживания уникальных курсоров

while True:
    try:
        # Отправляем запрос
        response = requests.post(url, headers=headers, cookies=cookies, data=payload)
        response_json = response.json()

        # Извлекаем данные
        data = response_json['data']['ad_library_main']['search_results_connection']['edges']

        # Логика обработки данных (пример)
        for node in data:
            # Обрабатываем node
            pass

        # Получаем следующий курсор
        next_cursor = response_json['data']['ad_library_main']['search_results_connection']['page_info'].get('end_cursor')
        print(f"Next cursor: {next_cursor}")

        # Проверяем, есть ли курсор
        if not next_cursor or next_cursor in seen_cursors:
            print("Cursor is missing or repeated. Stopping.")
            break

        # Обновляем список использованных курсоров
        seen_cursors.add(next_cursor)

        # Обновляем курсор в payload
        variables = json.loads(payload['variables'])  # Декодируем
        variables['cursor'] = next_cursor  # Обновляем курсор
        payload['variables'] = json.dumps(variables)  # Кодируем обратно
        print(f"Updated payload['variables']: {payload['variables']}")

    except json.JSONDecodeError:
        print("Failed to decode JSON. Response might not be valid.")
        break
    except Exception as e:
        print(f"Error: {e}")
        break
