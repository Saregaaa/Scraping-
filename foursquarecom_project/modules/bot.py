from load_django import *
from parser_app.models import *

import requests
import json

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
}

# for item in State.objects.filter(status='New').order_by('id'):

    # for i in range(30, 261, 30):
    
params = {
    "locale": "en",
    "explicit-lang": "false",
    "v": "20241112",
    "m": "foursquare",
    "intent": "food",
    "mode": "url",
    "limit": "30",
    # "offset": f"{i}",
    "noGeoSplitting": 1,
    # "near": f"{item.state}",
    "near": "11788",
    # "sw": "40.70823051511181,-74.17642593383789",
    # "ne": "40.80653332421558,-73.78023147583008",
    # "wsid": "0MQHCXQVDLWVPATMLHGNCIA2OUTRYD",
    "oauth_token": "QEJ4AQPTMMNB413HGNZ5YDMJSHTOHZHMLZCAQCCLXIX41OMP"
}

response = requests.get(url, headers=headers, params=params)
if response.status_code == 200:
    
        
    response.raise_for_status()
    data = response.json()
    print(data)
    
    with open('1.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
   

    
    try:
        for venue in data['response']['group']['results']:
            venue_data = venue['venue']
            
            menu_url = venue_data.get('menu', {}).get('url') or ''
            if len(menu_url) < 5:
                menu_url = None

            print('-' * 20)
            try:
                user_id = venue['photo']['user']['id'] if venue.get('photo') else None
                print(user_id)
            except Exception as e:
                user_id = None

            try:
                first_name = venue['photo']['user']['firstName'] if venue.get('photo') else None
                print(first_name)
            except Exception as e:
                first_name = None

            try:    
                last_name = venue['photo']['user']['lastName'] if venue.get('photo') else None
                print(last_name)
            except Exception as e:
                last_name = None

            try:
                private_profile = venue['photo']['user']['privateProfile'] if venue.get('photo') else None
                print(private_profile)
            except Exception as e:
                private_profile = None

            try:
                gender = venue['photo']['user']['gender'] if venue.get('photo') else None
                print(gender)
            except Exception as e:
                gender = None

            try:
                country_code = venue['photo']['user']['countryCode'] if venue.get('photo') else None
                print(country_code)
            except Exception as e:
                country_code = None

            try:
                following_relationship = venue['photo']['user']['followingRelationship'] if venue.get('photo') else None
                print(following_relationship)
            except Exception as e:
                following_relationship = None

            try:
                photo_prefix = venue['photo']['user']['photo']['prefix'] if venue.get('photo') else None
                photo_suffix = venue['photo']['user']['photo']['suffix'] if venue.get('photo') else None
                photo = photo_prefix + '360x360' + photo_suffix
                print(photo)
            except Exception as e:
                photo = None
            
            company_defaults = {
                'name': venue_data.get('name') or '',
                'url': venue_data.get('canonicalUrl') or '',
                'phone': venue_data.get('contact', {}).get('phone') or '',
                'address': venue_data.get('location', {}).get('address') or '',
                'city': venue_data.get('location', {}).get('city') or '',
                'state': venue_data.get('location', {}).get('state') or '',
                'postal_code': venue_data.get('location', {}).get('postalCode') or '',
                'category_name': venue_data.get('categories', [{}])[0].get('name') or '',
                'category_code': venue_data.get('categories', [{}])[0].get('id') or '',
                'category_icon': (venue_data.get('categories', [{}])[0].get('icon', {}).get('prefix', '') +
                                venue_data.get('categories', [{}])[0].get('icon', {}).get('suffix', '')) if venue_data.get('categories') else '',
                'rating': venue_data.get('rating') or '',
                'rating_signals': venue_data.get('ratingSignals') or '',
                'user_count': venue_data.get('stats', {}).get('usersCount') or '',
                'price_tier': venue_data.get('price', {}).get('tier') or '',
                'currency': venue_data.get('price', {}).get('currency') or '',
                'menu_url': menu_url,
                'user_id': user_id,
                'first_name': first_name,
                'last_name': last_name,
                'private_profile': private_profile,
                'gender': gender,
                'country_code': country_code,
                'following_relationship': following_relationship,
                'photo': photo,
                

                'popularity_by_geo': venue_data.get('popularityByGeo') or '',
                'context_geo_id': venue_data.get('location', {}).get('contextGeoId') or ''
            }

            Company.objects.get_or_create(
                url=company_defaults['url'], 
                defaults=company_defaults
                )
    except Exception as e:
        print(e)
    
    # item.status = 'Done'
    # item.save()

else:
    print(f"Ошибка при получении файла: {response.status_code}")

