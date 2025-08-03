from bs4 import BeautifulSoup
from load_django import *
from parser_app.models import *
import requests



headers = {
    "authority": "www.bahtsold.com",
    "method": "GET",
    "path": "/category/top/real-estate-1",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru,en-US;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "cookie": "PHPSESSID=hp45dbko5c28u8m0eotb2n6g7n; _gcl_au=1.1.1997012693.1732713109; _ga=GA1.2.1205117751.1732713109; _gid=GA1.2.612648845.1732713109; G_ENABLED_IDPS=google; _ga_C8Z4ETBKW7=GS1.2.1732713109.1.1.1732714358.0.0.0; __gads=ID=b958c9fd68eb1735:T=1732713108:RT=1732714358:S=ALNI_MazGHdFX3n9PHcDu_JHZQauGBdOjA; __gpi=UID=00000fa0cbd24dab:T=1732713108:RT=1732714358:S=ALNI_MaPmwUhPS8L9wjapYrQvhPtXTqOpQ; __eoi=ID=7bbfd0c3adf3d3b7:T=1732713108:RT=1732714358:S=AA-Afjbm8ho9Vozz4R0u_xpNOb6t; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2294b53b719af4d3196033f5afb0d8af2a%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%2231.128.162.188%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F131.0.0.0%20Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1732714358%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D6db58d27211f192902e77e8e49ac123e8cb14bf8",
    "priority": "u=0, i",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

for page in range(122, 130): #122

    print('page: ', page)
    print()
    
    # url = f"https://www.bahtsold.com/category/top/real-estate-{page}" #122
    url = f"https://www.bahtsold.com/quicksearch2?c=3&ca=1&pr_from=0&pr_to=NULL&top=1&s=&page={page}" #122


    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        print("Request was successful!")
        # print(response.text)  

        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("h4")

        if not links:
            print(f"На странице {page} нет ссылок. Прерываем цикл.")
            break

        for link in links:
            link = link.find("a")
            
            try:
                link = link['href']
                print('link: ', link)
                
            except (KeyError, TypeError):
                continue
            
            Link.objects.get_or_create(link=link)

    else:
        print(f"Error: {response.status_code}")
