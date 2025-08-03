from load_django import *
from parser_app.models import *
import requests
from bs4 import BeautifulSoup

import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from datetime import date, datetime, timedelta
from time import sleep

caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
# caps["pageLoadStrategy"] = "eager"  #  interactive
#caps["pageLoadStrategy"] = "none"



chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Активируем headless-режим
chrome_options.add_argument("--window-size=800,600")  # Устанавливаем размер окна

# chrome_options.page_load_strategy = 'normal'
# chrome_options.add_argument(r"--user-data-dir=modules/profile")
chrome_options.add_argument("--start-maximized")

for page in range(300, 600): # 300

    print('-' * 40)
    print('page: ', page)
    print()

    driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))


    # url = f"https://www.vivareal.com.br/aluguel/?pagina={page}"
    url = f"https://www.vivareal.com.br/venda/com-academia/?pagina={page}#com=academia"

    driver.get(url)
    sleep(4)

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup)

    links_ads = soup.find_all('a', class_='property-card__content-link js-card-title')

    for link_ads in links_ads:
        link_ads = link_ads.get('href')
        link_ads = f"https://www.vivareal.com.br{link_ads}"
       
        print('link_ads: ', link_ads)

        LinkAds.objects.get_or_create(link_ads=link_ads)