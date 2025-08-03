from load_django import *
from parser_app.models import *
import requests
from bs4 import BeautifulSoup
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',  
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'Trailers',  
}

for item in Product.objects.filter(status='New').order_by('id'):
# url = f'https://www.baldwinhardware.com/p/napa-handleset-x-ellipse-knob-square-interior?variant=sc-napxellxtsr-150'
    url = item.product_link

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    try:
        title = soup.h1.span.text.strip()
        print('Title: ', title)
    except Exception as e:
        title = None
        print('Title: ', title)

    try:
        model_number = soup.find('h6', class_='product-detail__model-number').text
        print('Model: ', model_number)
    except Exception as e:
        model_number = None
        print('Model: ', model_number)

    try:
        image_list = []
        images = soup.find_all('img', class_='product-detail__media')
        for image in images:
            image = image['src']
            image_list.append(image)
        print('Image: ', image_list)
    except Exception as e:
        image_list = None
        print('Image: ', image_list)

    try:
        key_features_list = []
        key_features_heading = soup.find('h5', string='Key Features')
        if key_features_heading:
            ul = key_features_heading.find_next('ul', class_='icons-list')
            if ul:
                features = ul.find_all('span', class_='icons-block__text')
                for feature in features:
                    # print('Key Feature: ', feature.get_text(strip=True))
                    key_features_list.append(feature.get_text(strip=True))
                print('Key Feature: ', key_features_list)
    except Exception as e:
        key_features_list = None
        print('Key Features: ', key_features_list)

    try:
        features_list = []
        features_heading = soup.find('h4', string='Features')
        if features_heading:
            ul = features_heading.find_next('ul', class_='icons-list')
            if ul:
                features = ul.find_all('span', class_='icons-block__text')
                for feature in features:
                    # print('Feature: ', feature.get_text(strip=True))
                    features_list.append(feature.get_text(strip=True))
                print('Feature: ', features_list)
    except Exception as e:
        features_list = None
        print('Features: ', features_list)

    try:
        spec_list = soup.find('ul', class_='spec-list')

        if spec_list:
            spec_items = spec_list.find_all('li', class_='spec-list__item')
            specifications_list = []
            for i in spec_items:
                title = i.find('div', class_='spec-list__title').get_text(strip=True)
                value_div = i.find('div', class_='spec-list__value')
                
                if value_div.find('ul'):
                    values = [li.get_text(strip=True) for li in value_div.find_all('li')]
                    value = values[0] if len(values) == 1 else values
                else:
                    value = value_div.get_text(strip=True)
                
                specifications_list.append((title, value))
            print('Specifications: ', specifications_list)
    except Exception as e:
        specifications_list = None
        print('Specifications: ', specifications_list)

    try:
        doc_list = soup.find('ul', class_='product-detail__product-doc-list')

        documents_list = []
        if doc_list:
            for i in doc_list.find_all('a', class_='product-detail__product-doc-link'):
                link = i.get('href', '#')  
                name = i.find('span', class_='product-detail__product-doc-name').get_text(strip=True) 
                if link != '#' and link.strip():
                    documents_list.append((name, link))
        print('Documents: ', documents_list)
    except Exception as e:
        documents_list = None
        print('Documents: ', documents_list)

       
    item.title = title
    item.model_number = model_number
    item.image_list = image_list
    item.key_features_list = key_features_list
    item.features_list = features_list
    item.specifications_list = specifications_list
    item.documents_list = documents_list
    item.status = 'Done'
    item.save()

 