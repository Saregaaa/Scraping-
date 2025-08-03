from load_django import *
from parser_app.models import *
import requests
from bs4 import BeautifulSoup



headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru,en-US;q=0.9,en;q=0.8",
    "referer": "https://aireaa.com/real-estate-agents?keyword=mum",
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


cookies = {
    "XSRF-TOKEN": "eyJpdiI6IjFLeDdlKzhBVW00dlJiL1d5S0RkOHc9PSIsInZhbHVlIjoiTkMwRmZCSnBKTkpUdEswTmxrVXBDM2dEb09Gb05aZ1h3ZHlnYkthVVlzSWZpdEVkQVNqY0IxK09qcTR1SEZKenVzV2Y0STVOSHMxWFY2Y3daeUtySk1JdzNTekhyVWJaRm1QL28rcncrazhRS0RvMk02K0hRaEc5aGd2VGdvTmoiLCJtYWMiOiI3Yzg2MDMxOGEzYjkyYmRmYzFmMTExZWRmNmViN2M0YWNhM2Q2OGEwMTc0YWQzZTNjNTEwMDgyOTBlY2Q5YTJjIiwidGFnIjoiIn0%3D",
    "aireaa_session": "eyJpdiI6IlduWDA0c0trZWRvYnAzQ1oyMG5aVWc9PSIsInZhbHVlIjoiV0ZBMG8vdXduT3RFUG1wUWhJOFVaQmdOK1JtYTMvUEF6dmJYa2xzRU5XZ3pXR1FDeXJBbThsR2dMRE5PYzdndEJjWkg1OGh1YmdYODEvbDJCTEo4NHNjR3FPaDBKVGxRWDgzTHN5M3dNc0xYTHdMem0wQnE4UHFra1A0di9aZk0iLCJtYWMiOiIwNjIyZjhmMWYyOThmZmUyYjgzM2ZjZGEyMGRlNzMwNzAxNjllNDBkNDY2MGRjMTI4ZTQxNjU1ZDI3OTA0OWI3IiwidGFnIjoiIn0%3D",
}

for page in range(100, 1173): # 1172
    print()
    print(f"Page: {page}")
    print()

    url = f"https://aireaa.com/real-estate-agents?page={page}"


    response = requests.get(url, headers=headers, cookies=cookies)


    if response.status_code == 200:
        print("Success!")

        soup = BeautifulSoup(response.text, "html.parser")
        agents_grid = soup.find_all("div", class_="agents-grid")

        unique_links = set()

        for grid in agents_grid:
            for link in grid.find_all("a"):
                href = link.get("href").strip()
                unique_links.add(href)

        for link in unique_links:
            print(link)

            if link:
                Agent.objects.get_or_create(link=link)

    else:
        print(f"Error: {response.status_code}")
