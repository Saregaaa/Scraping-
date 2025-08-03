from load_django import *
from parser_app.models import *

import requests
from bs4 import BeautifulSoup
import json


# Заголовки
headers = {
    "authority": "foursquare.com",
    "method": "GET",
    "path": "/v/kotobuki/4bf41fd3cad2c928a48b9b99",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "referer": "https://foursquare.com/explore?mode=url&near=11788%2C%20NY%2C%20%D0%A1%D1%88%D0%B0&nearGeoId=162411061564198940&q=%D0%9A%D0%B0%D1%84%D0%B5%20%D0%B8%20%D1%80%D0%B5%D1%81%D1%82%D0%BE%D1%80%D0%B0%D0%BD%D1%8B",
    "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

cookies = {
    "cookie": "_vwo_uuid_v2=DDDB41F06B871C31CAE953099E2197193|af7f457b17366c27990623027df079c7; _gcl_au=1.1.526747249.1731511514; bbhive=1QMDTMEJVXGE0PM5DIOILNQNCYE10E%3A%3A1794583567; _gid=GA1.2.1266117528.1731511605; OptanonAlertBoxClosed=2024-11-14T07:01:27.188Z; oauth_token=N5GBTRV4SNAVROJLPWJ3LVRKXVSEA1WY05ODMUYFPYOL3F5J-0; _ga_H5VDLC686V=GS1.2.1731654467.3.0.1731654467.0.0.0; _ga_13W256ZLLK=GS1.1.1731654469.2.0.1731654469.60.0.0; _ga_NRM9LCS9XM=GS1.1.1731654469.2.0.1731654469.60.0.0; _ga_3W40YQDD7J=GS1.1.1731654469.2.1.1731654469.60.0.0; _ga_F1K4V3ER0C=GS1.1.1731654469.2.0.1731654469.60.0.0; _ga=GA1.2.538307344.1731511515; _rdt_uuid=1731654471330.fbe94c12-149e-4ba5-9db7-9841c40f7e59; _hjSessionUser_1179695=eyJpZCI6Ijc0NmM1ZjkxLWI4ZGEtNTg0YS1iMThmLWUyNGRiNTU2NzdhNyIsImNyZWF0ZWQiOjE3MzE2NTQ0NzMwNzMsImV4aXN0aW5nIjpmYWxzZX0=; _ga_WS1DB07Q9P=GS1.2.1731671679.7.1.1731672027.0.0.0; XSESSIONID=1istsybf6wcirx4g0530xjdbk; PixelDensity=1; __utma=51454142.538307344.1731511515.1731672260.1731672260.1; __utmb=51454142.0.10.1731672260; __utmc=51454142; __utmz=51454142.1731672260.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=928f833f376ab659:T=1731654469:RT=1731672388:S=ALNI_Mamx_1zIrG6xgf0fURSRDd2SxlWaA; __gpi=UID=00000f957804c972:T=1731654469:RT=1731672388:S=ALNI_MZAjuF3K9NoVy95HpPgQgHhTKFLCw; __eoi=ID=c447ff19f92a03fb:T=1731513699:RT=1731672388:S=AA-AfjYU7L7R4JYNeOH5pBuNshs8; lc=%7B%22lat%22%3A40.39428%2C%22lng%22%3A-74.11709%2C%22loc%22%3A%22Middletown%22%2C%22cc%22%3A%22US%22%2C%22longGeoId%22%3A%2272057594043029106%22%7D; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Nov+15+2024+14%3A07%3A56+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=GB%3BENG; AWSALBTG=ayOLdDT+r2GJg05vKjoJ7GrDh90a8qSRkZZqhl3jIoHYWLhaTIYcwuEFp3p+WhnizI9qfy4IAxhYfICnFqsJADyLgQuN+LTpNj5r4CFuEIKTPIXrf6TflflZea0C8su8jXRPf0/70luC0lf44KEz2kwgNwV6u3SfkHenR6IlK8I7; AWSALBTGCORS=ayOLdDT+r2GJg05vKjoJ7GrDh90a8qSRkZZqhl3jIoHYWLhaTIYcwuEFp3p+WhnizI9qfy4IAxhYfICnFqsJADyLgQuN+LTpNj5r4CFuEIKTPIXrf6TflflZea0C8su8jXRPf0/70luC0lf44KEz2kwgNwV6u3SfkHenR6IlK8I7; AWSALB=VMM/3FCgkkkv4QJDg9vAcReHwh1I0xt4wQ8XQ23wqNu9LV+gU/6jFJ3N5BYXZ3sV3DoaGBnGriSMknBgeqVFmyrE2UAsdAfuTA0XgAD9dwjHQXxCVX1STey34yKn; AWSALBCORS=VMM/3FCgkkkv4QJDg9vAcReHwh1I0xt4wQ8XQ23wqNu9LV+gU/6jFJ3N5BYXZ3sV3DoaGBnGriSMknBgeqVFmyrE2UAsdAfuTA0XgAD9dwjHQXxCVX1STey34yKn; _ga_05JP5TT14W=GS1.2.1731672260.1.1.1731672479.0.0.0",
}

# URL запроса
url = "https://foursquare.com/marea2212916"


response = requests.get(url, headers=headers, cookies=cookies)


if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')
    # scripts = soup.find_all('script')

    # for script in scripts:
    #     if 'relatedVenuesResponse:' in script.text:
    #         print(script.text)
            
    #         with open('script1.txt', 'w', encoding='utf-8') as f:
    #             f.write(script.text)
    try:
        tel = soup.find('span', class_='tel').text
        print('Tel: ', tel)
    except Exception as e:
        tel = None
        print('Tel: ', tel)

    try:
        site = soup.find('a', class_='url')['href']
        print('Site: ', site)
    except Exception as e:
        site = None
        print('Site: ', site)

    try:
        facebook = soup.find('a', class_='facebookPageLink')['href']
        print('Facebook: ', facebook)
    except Exception as e:
        facebook = None
        print('Facebook: ', facebook)

    try:
        instagram = soup.find('a', class_='instagramPageLink')['href']
        print('Instagram: ', instagram)
    except Exception as e:
        instagram = None
        print('Instagram: ', instagram)

    try:
        twitter = soup.find('a', class_='twitterPageLink')['href']
        print('Twitter: ', twitter)
    except Exception as e:
        twitter = None
        print('Twitter: ', twitter)

    try:
        grubhub = soup.find('a', string='Заказ от Grubhub')['href']
        print('Grubhub: ', grubhub)
    except Exception as e:
        grubhub = None
        print('Grubhub: ', grubhub)

    try:
        reservation_link = soup.find('a', string='Make Reservation')['href']
        print('Reservation link: ', reservation_link)
    except Exception as e:
        reservation_link = None
        print('Reservation link: ', reservation_link)

    try:
        view_menu_on = soup.find('a', class_="menuLink")['href']
        print('View menu on: ', view_menu_on)
    except Exception as e:
        view_menu_on = None
        print('View menu on: ', view_menu_on)

    try:
        closed = soup.find('span', class_='closed').text
        print('Closed: ', closed)
    except Exception as e:
        closed = None
        print('Closed: ', closed)

    try:
        credit_card = soup.find('div', string='Credit Cards')
        credit_card = credit_card.find_next_sibling('div', class_='venueRowValue').text
        print('Credit card: ', credit_card)
    except Exception as e:
        credit_card = None
        print('Credit card: ', credit_card)

   
    try:
        reservation = soup.find('div', string='Reservations')
        reservation = reservation.find_next_sibling('div', class_='venueRowValue').text
        print('Reservation: ', reservation)
    except Exception as e:
        reservation = None
        print('Reservation: ', reservation)


    try:
        outdoor_places = soup.find('div', string='Outdoor Seating')
        outdoor_places = outdoor_places.find_next_sibling('div', class_='venueRowValue').text
        print('Outdoor places: ', outdoor_places)
    except Exception as e:
        outdoor_places = None
        print('Outdoor places: ', outdoor_places)

    try:
        drinking = soup.find('div', string='Drinks')
        drinking = drinking.find_next_sibling('div', class_='venueRowValue').text
        print('Drinking: ', drinking)
    except Exception as e:
        drinking = None
        print('Drinking: ', drinking)

    try:
        wifi = soup.find('div', string='WiFi')
        wifi = wifi.find_next_sibling('div', class_='venueRowValue').text
        print('Wifi: ', wifi)
    except Exception as e:
        wifi = None
        print('Wifi: ', wifi)

    try:
        menu = soup.find('div', string='Menus')
        menu = menu.find_next_sibling('div', class_='venueRowValue').text
        print('Menu: ', menu)
    except Exception as e:
        menu = None
        print('Menu: ', menu)

    try:
        parking = soup.find('div', string='Parking')
        parking = parking.find_next_sibling('div', class_='venueRowValue').text
        print('Parking: ', parking)
    except Exception as e:
        parking = None
        print('Parking: ', parking)

    try:
        restroom = soup.find('div', string='Restroom')
        restroom = restroom.find_next_sibling('div', class_='venueRowValue').text
        print('Restroom: ', restroom)
    except Exception as e:
        restroom= None
        print('Restroom: ', restroom)

    try:
        music = soup.find('div', string='Music')
        music = music.find_next_sibling('div', class_='venueRowValue').text
        print('Music: ', music)
    except Exception as e:
        music = None
        print('Music: ', music)

    try:
        accessible = soup.find('div', string='Wheelchair Accessible')
        accessible = accessible.find_next_sibling('div', class_='venueRowValue').text
        print('Wheelchair accessible: ', accessible)
    except Exception as e:
        accessible = None
        print('Wheelchair accessible: ', accessible)

    

    # credit_card = soup.find('a', string='Кредитные карты').find_next_sibling('div', class_='venueRowValue').text
    # print('Кредитные карты: ', credit_card)

    # credit_card = soup.find('div', {'class': 'sideVenueBlockRow sideVenueAttributeRow'})
    # if credit_card:
    #     key = credit_card.find('div', class_='venueRowKey')
    #     value = credit_card.find('div', class_='venueRowValue')
    #     if key and value and 'Кредитные карты' in key.text:
    #         print('Кредитные карты:', value.text)


else:
    print(f"Ошибка при получении файла: {response.status_code}")
