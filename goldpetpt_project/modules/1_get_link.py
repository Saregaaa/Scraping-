from load_django import *
from parser_app.models import *

import requests
import json


headers = {
    "authority": "goldpet.pt",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru,en-US;q=0.9,en;q=0.8",
    "cookie": "PHPSESSID=n2ikf4t64dlnmjakd1oput96in; GOLDPET-591644096bab2e34fc10f55e54f9f16d=def50200375c88cdc171675fae0327f76229247f6aa1fb34d941452cf5fead30974e0254d259ed8a65aebd12ce2c621bf7c52f9e934c2c00c6ad815e4fdcfcc8114b8f54b3ce53676fa150c6a86a29c4a36a9ca087817dc53ae180441b9cb876046d2c9615edbada485fb19d3ebcc77079b42467d02c5017fca5aed0b8c3a362f4c4599a65d5ed0a62e64c432329935ddc449ffc968baa2619e3f83af98b27100e9829db965a2397aaf3c69558a54c28dc99a5cafa785b6567c30d555299c6bf43449333c0f0bbbfb481a9fc47b7471a2fa91f695586fad932",
    "referer": "https://goldpet.pt/4-gato",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

category_main = "Cão"
category_slug = "3-cao"

url = f"https://goldpet.pt/{category_slug}"

for page in range(1, 3): # 40

    print()
    print('Page: ', page)
    print()
   
    params = {
        "page": page
    }


    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print("Success!")
        # print(response.json())  

        data = response.json()
        # with open(f'files/1_get_api_goldpetpt{page}.json', 'w') as f:
        #     json.dump(data, f, indent=4)
        products = data['products']

        for product in products:
            
            try:
                name = product['name']
            except Exception:
                name = None

            try:
                id_product = product['id_product']
            except Exception:
                id_product = None

            try:
                price = product['price']
            except Exception:
                price = None

            try:
                description_short = product['description_short']
            except Exception:
                description_short = None

            try:
                category_name = product['category_name']
            except Exception:
                category_name = None

            try:
                link = product['link']
            except Exception:
                link = None

            try:
                image = product['cover']['large']['url']
            except Exception:
                image = None

            try:
                discount_percentage_absolute = product['discount_percentage_absolute']
            except Exception:
                discount_percentage_absolute = None

            try:
                regular_price_amount = product['regular_price_amount']
            except Exception:
                regular_price_amount = None

            print('ID: ', id_product)
            print('Name: ', name)
            print('Price: ', price)
            print('Category: ', category_name)
            print('Description: ', description_short)
            print('Discount: ', discount_percentage_absolute)
            print('Regular price: ', regular_price_amount)
            print('Image: ', image)
            print('Link: ', link)
            print()

            Product.objects.get_or_create(
                id_product = id_product,
                name = name,
                link = link,
                category_main = category_main,
                defaults = {
                    'price': price,
                    'description_short': description_short,
                    'category_name': category_name,
                    'image': image,
                    # 'discount_percentage_absolute': discount_percentage_absolute,
                    # 'regular_price_amount': regular_price_amount
                }
            )

    else:
        print(f"Error: {response.status_code}")
        print(response.text)  
