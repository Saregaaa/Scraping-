from load_django import *
from parser_app.models import *
import requests
import json


url = "https://www.baldwinhardware.com/api/bh/product-filtering"


headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": "language=en; ARRAffinity=44807e4adf1fc10dc00e359aacf67824f79b62ac25d92840d3384c178347a44a; ARRAffinitySameSite=44807e4adf1fc10dc00e359aacf67824f79b62ac25d92840d3384c178347a44a; _ga=GA1.1.1840293677.1732214203; BVImplmain_site=0802; _ga_B49Z4Z7SJ0=GS1.1.1732214202.1.1.1732218432.23.0.0",
    "Host": "www.baldwinhardware.com",
    "Origin": "https://www.baldwinhardware.com",
    "Pragma": "no-cache",
    "Referer": "https://www.baldwinhardware.com/sc/tubular-handlesets",
    "Sec-CH-UA": '"Chromium";v="128", "Not;A=Brand";v="24", "Opera GX";v="114"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0"
}

for page in range(0, 40):
    
    payload = {
        "category": None,
        "productSlug": None,
        "filterOptions": {
            "pageNumber": page,
            "sort": "Featured"
        },
        "filters": None
    }


    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Success:")
        data = response.json()

        products = data['data']['products']
        for product in products:
            product_link = product['productDetailUrl']
            product_link = 'https://www.baldwinhardware.com' + product_link
            print(product_link)

            Product.objects.get_or_create(product_link=product_link)

    else:
        print(f"Error: {response.status_code}")
        print(response.text)
