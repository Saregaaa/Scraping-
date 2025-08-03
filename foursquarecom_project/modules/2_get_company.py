from load_django import *
from parser_app.models import *

import requests
import json
from time import sleep

url = "https://api.foursquare.com/v2/search/recommendations"
# file_path = r'modules\foursquare_recommendations.json'


headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://foursquare.com",
    "referer": "https://foursquare.com/",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

proxies = {
        "http": "http://rgjbrtfk-rotate:bvltatsjhych@p.webshare.io:80/",
        "https": "http://rgjbrtfk-rotate:bvltatsjhych@p.webshare.io:80/"
    }

for item in ZipCode.objects.filter(status='New').order_by('id'):
    # sleep(0.5)
    for i in range(0, 121, 30):
        # sleep(0.5)
        params = {
            "locale": "en",
            "explicit-lang": "false",
            "v": "20241112",
            "m": "foursquare",
            "intent": "food",
            "mode": "url",
            "limit": "30",
            "offset": f"{i}",
            "noGeoSplitting": 1,
            # "near": f"{item.state}",
            "near": f"{item.zip_code}",
            # "sw": "40.70823051511181,-74.17642593383789",
            # "ne": "40.80653332421558,-73.78023147583008",
            # "wsid": "0MQHCXQVDLWVPATMLHGNCIA2OUTRYD",
            # "oauth_token": "QEJ4AQPTMMNB413HGNZ5YDMJSHTOHZHMLZCAQCCLXIX41OMP"
            # "oauth_token": "N5GBTRV4SNAVROJLPWJ3LVRKXVSEA1WY05ODMUYFPYOL3F5J"
            "oauth_token": "QEJ4AQPTMMNB413HGNZ5YDMJSHTOHZHMLZCAQCCLXIX41OMP"
        }

        response = requests.get(url, headers=headers, params=params, proxies=proxies)
        if response.status_code == 200:
            print(item.zip_code)
                
            response.raise_for_status()
            data = response.json()
            # print(data)
            
            with open('1.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            
            try:
                if data['response']['group']['results'][0]['venue']['id'] == None:
                    print('No data')
                    item.status = 'Done'
                    item.save()
                    break
            except Exception as e:
                print('No data')
                item.status = 'Done'
                item.save()
                break
            
            try:
                for venue in data['response']['group']['results']:

                    print('-' * 20)

                    try:
                        venue_id = venue['id'] 
                        print('venue_id: ', venue_id)
                    except Exception as e:
                        venue_id = None
                        print('venue_id: ', venue_id)
                    
                    
                    try:
                        user_id = venue['photo']['user']['id'] 
                        print('user_id: ', user_id)
                    except Exception as e:
                        user_id = None
                        print('user_id: ', user_id)

                    try:
                        first_name = venue['photo']['user']['firstName'] 
                        print('first_name: ', first_name)
                    except Exception as e:
                        first_name = None
                        print('first_name: ', first_name)

                    try:    
                        last_name = venue['photo']['user']['lastName'] 
                        print('last_name: ', last_name)
                    except Exception as e:
                        last_name = None
                        print('last_name: ', last_name)

                    try:
                        private_profile = venue['photo']['user']['privateProfile'] 
                        print('private_profile: ', private_profile)
                    except Exception as e:
                        private_profile = None
                        print('private_profile: ', private_profile)

                    try:
                        gender = venue['photo']['user']['gender'] 
                        print('gender: ', gender)
                    except Exception as e:
                        gender = None
                        print('gender: ', gender)

                    try:
                        country_code = venue['photo']['user']['countryCode'] 
                        print('country_code: ', country_code)
                    except Exception as e:
                        country_code = None
                        print('country_code: ', country_code)

                    try:
                        following_relationship = venue['photo']['user']['followingRelationship'] 
                        print('following_relationship: ', following_relationship)
                    except Exception as e:
                        following_relationship = None
                        print('following_relationship: ', following_relationship)

                    try:
                        photo_prefix = venue['photo']['user']['photo']['prefix'] 
                        photo_suffix = venue['photo']['user']['photo']['suffix'] 
                        photo = photo_prefix + '360x360' + photo_suffix
                        print('photo: ', photo)
                    except Exception as e:
                        photo = None
                        print('photo: ', photo)
                    
                    try:
                        name = venue['venue']['name']
                        print('name: ', name)
                    except Exception as e:
                        name = None
                        print('name: ', name)

                    try:
                        link = venue['photo']['user']['canonicalUrl']
                        print('link: ', link)
                    except Exception as e:
                        link = None
                        print('link: ', link)

                    try:
                        phone = venue['venue']['contact']['phone']
                        print('phone: ', phone)
                    except Exception as e:
                        phone = None
                        print('phone: ', phone)

                    try:
                        address = venue['venue']['location']['address']
                        print('address: ', address)
                    except Exception as e:
                        address = None
                        print('address: ', address)

                    try:
                        city = venue['venue']['location']['city']
                        print('city: ', city)
                    except Exception as e:
                        city = None
                        print('city: ', city)

                    try:
                        state = venue['venue']['location']['state']
                        print('state: ', state)
                    except Exception as e:
                        state = None
                        print('state: ', state)

                    try:
                        postal_code = venue['venue']['location']['postalCode']
                        print('postal_code: ', postal_code)
                    except Exception as e:
                        postal_code = None
                        print('postal_code: ', postal_code)

                    try:
                        category_name = venue['venue']['categories'][0]['name']
                        print('category_name: ', category_name)
                    except Exception as e:
                        category_name = None
                        print('category_name: ', category_name)

                    try:
                        category_code = venue['venue']['categories'][0]['id']
                        print('category_code: ', category_code)
                    except Exception as e:
                        category_code = None
                        print('category_code: ', category_code)

                    try:
                        rating = venue['venue']['rating']
                        print('rating: ', rating)
                    except Exception as e:
                        rating = None
                        print('rating: ', rating)

                    try:
                        rating_signals = venue['venue']['ratingSignals']
                        print('rating_signals: ', rating_signals)
                    except Exception as e:
                        rating_signals = None
                        print('rating_signals: ', rating_signals)

                    try:
                        user_count = venue['venue']['stats']['usersCount']
                        print('user_count: ', user_count)
                    except Exception as e:
                        user_count = None
                        print('user_count: ', user_count)

                    try:
                        price_tier = venue['venue']['price']['tier']
                        print('price_tier: ', price_tier)
                    except Exception as e:
                        price_tier = None
                        print('price_tier: ', price_tier)

                    try:
                        currency = venue['venue']['price']['currency']
                        print('currency: ', currency)
                    except Exception as e:
                        currency = None
                        print('currency: ', currency)

                    try:
                        menu_url = venue['venue']['menu']['url']
                        print('menu_url: ', menu_url)
                    except Exception as e:
                        menu_url = None
                        print('menu_url: ', menu_url)

                    try:
                        popularity_by_geo = venue['venue']['popularityByGeo']
                        print('popularity_by_geo: ', popularity_by_geo)
                    except Exception as e:
                        popularity_by_geo = None
                        print('popularity_by_geo: ', popularity_by_geo)
                    
                    try:
                        context_geo_id = venue['venue']['location']['contextGeoId']
                        print('context_geo_id: ', context_geo_id)
                    except Exception as e:
                        context_geo_id = None
                        print('context_geo_id: ', context_geo_id)

                    company_defaults = {
                        'name': name,
                        'link': link,
                        'phone': phone,
                        'address': address,
                        'city': city,
                        'state': state,
                        'postal_code': postal_code,
                        'category_name': category_name,
                        'category_code': category_code,
                        'rating': rating,
                        'rating_signals': rating_signals,
                        'user_count': user_count,
                        'price_tier': price_tier,
                        'currency': currency,
                        'menu_url': menu_url,
                        'user_id': user_id,
                        'first_name': first_name,
                        'last_name': last_name,
                        'private_profile': private_profile,
                        'gender': gender,
                        'country_code': country_code,
                        'following_relationship': following_relationship,
                        'photo': photo,
                        'popularity_by_geo': popularity_by_geo,
                        'context_geo_id': context_geo_id,
                        'status': 'Done'
                    }

                    Company.objects.get_or_create(
                        venue_id=venue_id,
                        defaults=company_defaults,
                        )
                    
            except Exception as e:
                print(e)
            
            item.status = 'Done'
            item.save()

        else:
            print(f"Ошибка при получении файла: {response.status_code}")

