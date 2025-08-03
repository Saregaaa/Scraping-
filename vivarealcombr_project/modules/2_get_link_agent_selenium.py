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
chrome_options.add_argument("--window-size=800,600")  # Устанавливаем размер окна
# chrome_options.page_load_strategy = 'normal'
# chrome_options.add_argument(r"--user-data-dir=modules/profile")
chrome_options.add_argument("--start-maximized")

for item in LinkAds.objects.filter(status='New').order_by('id'):

    driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
    
    url = item.link_ads
    # url = "https://www.vivareal.com.br/imovel/casa-3-quartos-vila-formosa-zona-leste-sao-paulo-com-garagem-127m2-aluguel-RS3300-id-2752731899/"

    driver.get(url)
    # sleep(4)

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup)
    try:
        link = soup.find('a', class_='l-link l-link--context-neutral l-link--underlined advertiser-header__credentials_name advertiser-header__link').get('href')
        print(link)  
        if link:
            LinkAgent.objects.get_or_create(link=link)
        else:
            print("Ссылка не найдена")
    except (AttributeError, TypeError):
        print('link not found')                  


    item.status = 'Done'
    item.save()

  