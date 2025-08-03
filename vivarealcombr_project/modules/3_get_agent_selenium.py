from load_django import *
from parser_app.models import *
import requests
from bs4 import BeautifulSoup
import re

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


for item in LinkAgent.objects.filter(status='New').order_by('id'):

    driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
    
    url = item.link

    # url = "https://www.vivareal.com.br/642787/auxiliadora-predial-alugueis-floresta/"

    driver.get(url)

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup)

    scripts = soup.find_all('script')

    for script in scripts:
        # print(script)
        
        if "window.__SETTINGS__" in script.text:
            content = script.text
            # print(content)
            try:
                data = content.split('"condominium":null,"redirectRule":null},')[1].split(',"createdDate"')[0]
            except IndexError:
                print('IndexError')
            
           
            data = '{' + data + '}}'
            
            # print(data)

            # Парсим в JSON
            try:
                json_data = json.loads(data)
                # print(json_data)
            except json.JSONDecodeError as e:
                print("Ошибка при конвертации в JSON:", e)

            try:
                account_name = json_data['account']['name']
                print('account_name: ', account_name)
            except KeyError:
                account_name = None
                print('account_name: ', account_name)

            try:
                account_id = json_data['account']['legacyVivarealId']
                print('account_id: ', account_id)
            except KeyError:
                account_id = None
                print('account_id: ', account_id)

            try:
                license_number = json_data['account']['licenseNumber']
                print('license_number: ', license_number)
            except KeyError:
                license_number = None
                print('license_number: ', license_number)

            try:
                phone_primary = json_data['account']['phones']['primary']
                print('phone_primary: ', phone_primary)
            except KeyError:
                phone_primary = None
                print('phone_primary: ', phone_primary)

            try:
                phone_mobile = json_data['account']['phones']['mobile']
                print('phone_mobile: ', phone_mobile)
            except KeyError:
                phone_mobile = None
                print('phone_mobile: ', phone_mobile)

            try:
                website_url = json_data['account']['websiteUrl']
                print('website_url: ', website_url)
            except KeyError:
                website_url = None
                print('website_url: ', website_url)

            try:
                country = json_data['account']['addresses']['shipping']['country']
                print('country: ', country)
            except KeyError:
                country = None
                print('country: ', country)

            try:
                zip_code = json_data['account']['addresses']['shipping']['zipCode']
                print('zip_code: ', zip_code)
            except KeyError:
                zip_code = None
                print('zip_code: ', zip_code)

            try:
                city = json_data['account']['addresses']['shipping']['city']
                print('city: ', city)
            except KeyError:
                city = None
                print('city: ', city)

            try:
                street_number = json_data['account']['addresses']['shipping']['streetNumber']
                print('street_number: ', street_number)
            except KeyError:
                street_number = None
                print('street_number: ', street_number)

            try:
                street = json_data['account']['addresses']['shipping']['street']
                print('street: ', street)
            except KeyError:
                street = None
                print('street: ', street)

            try:
                state = json_data['account']['addresses']['shipping']['state']
                print('state: ', state)
            except KeyError:
                state = None
                print('state: ', state)

            try:
                neighborhood = json_data['account']['addresses']['shipping']['neighborhood']
                print('neighborhood: ', neighborhood)
            except KeyError:
                neighborhood = None
                print('neighborhood: ', neighborhood)

            try:
                logo_url = soup.find('div', class_='teaser__publisher-logo').find('img')['src']
                print('logo_url: ', logo_url)
            except (AttributeError, KeyError):
                logo_url = None
                print('logo_url: ', logo_url)
        
            link = url


            defaults = {
                'account_name': account_name,
                'account_id': account_id,
                'license_number': license_number,
                'phone_primary': phone_primary,
                'phone_mobile': phone_mobile,
                'website_url': website_url,
                'country': country,
                'zip_code': zip_code,
                'city': city,
                'street_number': street_number,
                'street': street,
                'state': state,
                'neighborhood': neighborhood,
                'logo_url': logo_url,
                'status': 'Done'
            }

            Agent.objects.get_or_create(
                link=link, 
                defaults=defaults
                )
            
            item.status = 'Done'
            item.save()

        

