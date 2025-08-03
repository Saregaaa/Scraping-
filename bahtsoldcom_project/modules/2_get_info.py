from bs4 import BeautifulSoup
from load_django import *
from parser_app.models import *
import requests


headers = {
    "authority": "www.bahtsold.com",
    "method": "GET",
    "path": "/view/impressive-detached-villa-and-pool-for-sale--533707",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru,en-US;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "cookie": (
        "PHPSESSID=hp45dbko5c28u8m0eotb2n6g7n; _gcl_au=1.1.1997012693.1732713109; "
        "_ga=GA1.2.1205117751.1732713109; _gid=GA1.2.612648845.1732713109; "
        "G_ENABLED_IDPS=google; __gads=ID=b958c9fd68eb1735:T=1732713108:RT=1732715395:S=ALNI_MazGHdFX3n9PHcDu_JHZQauGBdOjA; "
        "__gpi=UID=00000fa0cbd24dab:T=1732713108:RT=1732715395:S=ALNI_MaPmwUhPS8L9wjapYrQvhPtXTqOpQ; "
        "__eoi=ID=7bbfd0c3adf3d3b7:T=1732713108:RT=1732715395:S=AA-Afjbm8ho9Vozz4R0u_xpNOb6t; "
        "ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2274a827c3c2738018959d3f32b2c22f32%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%2231.128.162.188%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F131.0.0.0%20Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1732715648%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D65da3b217716b3462bbf6e1d394f528f599d418e; "
        "_ga_C8Z4ETBKW7=GS1.2.1732713109.1.1.1732715651.0.0.0"
    ),
    "priority": "u=0, i",
    "referer": "https://www.bahtsold.com/category/top/real-estate-1?page=1",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

for item in Link.objects.filter(status='Done'):
    print()
    print(item.link)
    print()

    url = item.link
# url = "https://www.bahtsold.com/view/impressive-detached-villa-and-pool-for-sale--533707"

    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        print("Request was successful!")

        soup = BeautifulSoup(response.text, "html.parser")

        user_widget = soup.find("div", class_="user-widget")
        try:
            name = user_widget.find("h4").text.strip()
            print('name: ', name)
        except AttributeError:
            name = None
            print('name: ', name)

        try:
            calendar = user_widget.find("div", class_="block-user-detail").find('div').text.strip()
            print('calendar: ', calendar)
        except AttributeError:
            calendar = None
            print('calendar: ', calendar)

        try:
            customer = user_widget.find("div", class_="customer-widget").text.strip()
            print('customer: ', customer)
        except AttributeError:
            customer = None
            print('customer: ', customer)

        phone = None    
        try:
            scripts = soup.find_all('script')
            for script in scripts:
                if 'show_phone_number' in script.text:
                    # print('script: ', script.text)
                    phone = script.text.split("html('")[1].split("');")[0]
                    print('phone: ', phone)
        except AttributeError:
            phone = None
            print('phone: ', phone)


        try:
            website_link_tag = soup.find('a', title="Visit Website")
            website_link = website_link_tag.get('href')
            print("website_link:", website_link)
        except AttributeError:
            website_link = None
            print("website_link:", website_link)


        try:
            profile_link = soup.find('a', class_="link")
            profile_link = profile_link.get('href')
            print("profile_link:", profile_link)
        except AttributeError:
            profile_link = None
            print("profile_link:", profile_link)

        if profile_link:
            Customer.objects.get_or_create(
                profile_link = profile_link,
                defaults={
                    'name': name,
                    'customer': customer,
                    'phone': phone,
                    'website_link': website_link,
                    'calendar': calendar
                }
            )


        CustomerDub.objects.get_or_create(
            link_sale=item.link,
            defaults={
                'profile_link': profile_link,
                'name': name,
                'customer': customer,
                'phone': phone,
                'website_link': website_link,
                'calendar': calendar
            }
        )

        item.status = 'Done1'
        item.save()


    else:
        print(f"Error: {response.status_code}")
