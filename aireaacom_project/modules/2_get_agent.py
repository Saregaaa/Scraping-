from load_django import *
from parser_app.models import *
import requests
from bs4 import BeautifulSoup



headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru,en-US;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "referer": "https://aireaa.com/real-estate-agents?page=2",
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
    "XSRF-TOKEN": "eyJpdiI6IkVSNnpaSWZMQW9SZW5FMmMza01oc3c9PSIsInZhbHVlIjoiYnNpeFE4SFR4V1E3aXNFbGpMcU9DdHFKNVo5WWNxWG1vTnBPNnE2Y0c5Yi9mY2huUEhabGdHdmhJbUNCMU5pY0xkdUxjcnBVVWZrc2pFbWpwNjUvOGZhWGJlanFQQk9UYm9WbnE4eUh6WUJWWlV2am44UjFnUURlaDEwOTBvbnMiLCJtYWMiOiI4YWJhNjE3ZGM3OWEzOTQ4ODI0MmJlODQyNzRhZjBmZTEwM2MwZTUzZDk3MjlkMTVhNzYzZmNjMmM3YzUxOWQ3IiwidGFnIjoiIn0%3D",
    "aireaa_session": "eyJpdiI6IkdhR3hvcUdmaUZXbEZuVW42QW5TZXc9PSIsInZhbHVlIjoiMzJUOERmV01QUHFQaEVvUkZyS3FXQnZqSEg5cForSGxkRSszNGd1L3Z0NkN6ZnMwVW0xVkdpd0JMQy9YUFJTWE5id1NoUWR5ZGdRdUtqYVZwTlJFc3FUTGwwYTV5bm83OWVHTkJuTkQ3LzhYK1puRG1uSFVPTUE4VmtOd1B4d2giLCJtYWMiOiI1ZmJkNGE2ODlhYjM0ODE3OTY1ZTUyMThiMjRmNmNhNzJmMzAxMjE1YzAxY2IzMGZiZTg2ODc4Mjk5M2M5OGNmIiwidGFnIjoiIn0%3D",
}


for item in Agent.objects.filter(status="New").order_by("id"):
    
    print()
    print(item.link)
    print()

    # url = "https://aireaa.com/real-estate-agent-detail/63405"
    url = item.link

    response = requests.get(url, headers=headers, cookies=cookies)


    if response.status_code == 200:
        print("Success!")
        # print(response.text)  
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            agent_name = soup.find("div", class_="agency-name").find("h4").text
        except AttributeError:
            agent_name = None
        print('Agent name:', agent_name)

        try:
            address = soup.find("div", class_="agency-name").find("span").text
        except AttributeError:
            address = None
        print('Address:', address)

        try:
            description = soup.find("div", class_="agency-desc").text.strip()
        except AttributeError:
            description = None
        print('Description:', description)

        try:
            photo = soup.find("div", class_="agency-avatar").find("img")["src"]
            if photo == "https://aireaa.com/assets/img/dummy.jpg":
                photo = None
        except AttributeError:
            photo = None
        print('Photo:', photo)

        try:
            company_name = soup.find("strong", string="Company Name").find_next("div").text
        except AttributeError:
            company_name = None
        print('Company name:', company_name)

        try:
            phone = soup.find("strong", string="Phone Number").find_next("div").text.strip()
        except AttributeError:
            phone = None
        print('Phone:', phone)

        try:
            office_phone = soup.find("strong", string="Office Number").find_next("div").text.strip()
        except AttributeError:
            office_phone = None
        print('Office_phone:', office_phone)

        try:
            email = soup.find("strong", string="Email Address").find_next("div").text.strip()
        except AttributeError:
            email = None
        print('Email:', email)

        try:
            city = soup.find("strong", string="City").find_next("div").text.strip()
        except AttributeError:
            city = None
        print('City:', city)

        try:
            operating_area = soup.find("strong", string="Operating Area").find_next("div").text
            operating_area = ''.join(operating_area.split())
            operating_area = operating_area.replace(",", ", ")
        except Exception:
            operating_area = None
        print('Operating_area:', operating_area)


        item.agent_name = agent_name
        item.address = address
        item.description = description
        item.photo = photo
        item.company_name = company_name
        item.phone = phone
        item.office_phone = office_phone
        item.email = email
        item.city = city
        item.operating_area = operating_area
        item.status = "Done"
        item.save()


    else:
        print(f"Error: {response.status_code}")
