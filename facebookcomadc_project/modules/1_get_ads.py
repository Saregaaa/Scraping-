from load_django import *
from parser_app.models import *
import requests
import json
import datetime
from time import sleep


KEYWORD = "ads"

# URL for the POST request
url = "https://www.facebook.com/api/graphql/"

# Full headers
headers = {
    "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.facebook.com",
    "pragma": "no-cache",
    "referer": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&media_type=all&q=brianna&search_type=keyword_unordered",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-full-version-list": '"Google Chrome";v="131.0.6778.69", "Chromium";v="131.0.6778.69", "Not_A Brand";v="24.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Linux"',
    "sec-ch-ua-platform-version": '"6.8.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-asbd-id": "129477",
    "x-fb-friendly-name": "AdLibrarySearchPaginationQuery",
    "x-fb-lsd": "5sy4PbExRZsXwUb0_0jDuo",
}

# Full cookies
cookies = {
    "datr": "6YNNZjcT22BX_q1cmcvweHuo",
    "sb": "QfJOZgvom_J8GZWy-d9wAG4i",
    "c_user": "100016622866824",
    "ps_l": "1",
    "ps_n": "1",
    "dpr": "2",
    "ar_debug": "1",
    "fr": "19UzrKMxQNf4MbWmc.AWWVEg0J3nHUF1FnDxdi4xUmtXA.BnQtBU..AAA.0.0.BnQtBU.AWVRgSUzjo4",
    "xs": "48%3AVkgIFX0bWNgFSA%3A2%3A1719554535%3A-1%3A16378%3A%3AAcVRB7vNRq6_n0RaSDyRrp0j7R1D9ugW82HkEW_HCmo",
    "wd": "1850x498",
}

# Full payload
payload = {
    "av": "100016622866824",
    "__aaid": "0",
    "__user": "100016622866824",
    "__a": "1",
    "__req": "11",
    "__hs": "20051.HYP:comet_plat_default_pkg.2.1..2.1",
    "dpr": "2",
    "__ccg": "MODERATE",
    "__rev": "1018452212",
    "__s": "s16wj6:e46s1g:9xzj6p",
    "__hsi": "7440738787576568825",
    "__dyn": "7xeUmxa13yoS1syUbFp432m2q1Dxu13wqovzEdF8ixy360CEbo9E3-xS6Ehw2nVEK12wvk0ie2O1VwBwXwEwgo9oO0iS12x62G3i1ywOwv89k2C1FwaG5E6i588Egz898mwkE-U6-3e4UaEW0KrK2S1qxaawse5o4q0HUkw4BwMzUdEGdwzwea0K-1Lwqp8aE2cwAwQwr86C0nC1TwmUaE2Tw",
    "__csr": "isy949aFeCjJRy8KnzQHhpbHKUHOaG9VaCnLyoiye484eU6e1rxC3W2y0Lo1883ewYw9e04tE00Hfq1Mw",
    "__comet_req": "1",
    "fb_dtsg": "NAcP05RRMNny7GXpdoWG75cJtB-EA5e0zyq9i3jLifOGcYO1ttiEW_A:48:1719554535",
    "jazoest": "25338",
    "lsd": "5sy4PbExRZsXwUb0_0jDuo",
    "__spin_r": "1018452212",
    "__spin_b": "trunk",
    "__spin_t": "1732432001",
    "__jssesw": "1",
    "fb_api_caller_class": "RelayModern",
    "fb_api_req_friendly_name": "AdLibrarySearchPaginationQuery",
    "variables": json.dumps({
            "activeStatus":"active",
            "adType":"ALL",
            "bylines":[],
            "collationToken":"064e40b2-a8de-41e8-956b-e60fc221fcc1",
            "contentLanguages":[],
            "countries":["US"],
            "cursor":"AQHRFCH3aNcESm4VDx4GmcQeU8sRy5-4ATDDwQ7TFU2fCp6GouHMQkpPOF7JbprmIGJ8",
            "excludedIDs":None,
            "first":30,
            "location":None,
            "mediaType":"all",
            "pageIDs":[],
            "potentialReachInput":None,
            "publisherPlatforms":[],
            "queryString":f"{KEYWORD}",
            "regions":None,
            "searchType":"keyword_unordered",
            "sessionID":"400a5cf0-44ee-4158-93f6-b120b1de3aac",
            "sortData":None,
            "source":None,
            "startDate":None,
            "v":"ac8592",
            "viewAllPageID":"0"
        }),
    "server_timestamps": "true",
    "doc_id": "27545919331688429",
}


while True:
    
    try:
        response = requests.post(url, headers=headers, cookies=cookies, data=payload)
        sleep(1)
        response_json = response.json()
        # print('response_json: ', response_json)

        data = response_json['data']['ad_library_main']['search_results_connection']['edges']
        for node in data:
            node = node['node']

            try:
                ad_archive_id = node['collated_results'][0]['ad_archive_id']
                print('ad_archive_id: ', ad_archive_id)
            except (KeyError, TypeError):
                ad_archive_id = None
                print('ad_archive_id: ', ad_archive_id)

            try:
                collation_id = node['collated_results'][0]['collation_id']
                print('collation_id: ', collation_id)
            except (KeyError, TypeError):
                collation_id = None
                print('collation_id: ', collation_id)

            try:
                page_id = node['collated_results'][0]['page_id']
                print('page_id: ', page_id)
            except (KeyError, TypeError):
                page_id = None
                print('page_id: ', page_id)

            try:
                page_name = node['collated_results'][0]['page_name']
                print('page_name: ', page_name)
            except (KeyError, TypeError):
                page_name = None
                print('page_name: ', page_name)

            try:
                title = node['collated_results'][0]['snapshot']['title']
                print('title: ', title)
            except (KeyError, TypeError):
                title = None
                print('title: ', title)
            
            try:
                body = node['collated_results'][0]['snapshot']['body']['text']
                body = ' '.join(body.split())
                print('body: ', body)
            except (KeyError, TypeError):
                body = None
                print('body: ', body)

            try:
                caption = node['collated_results'][0]['snapshot']['caption']
                print('caption: ', caption)
            except (KeyError, TypeError):
                caption = None
                print('caption: ', caption)

            try:
                link_description = node['collated_results'][0]['snapshot']['link_description']
                print('link_description: ', link_description)
            except (KeyError, TypeError):
                link_description = None
                print('link_description: ', link_description)

            try:
                link_url = node['collated_results'][0]['snapshot']['link_url']
                print('link_url: ', link_url)
            except (KeyError, TypeError):
                link_url = None
                print('link_url: ', link_url)
            
            try:
                images = node['collated_results'][0]['snapshot']['images'][0]['original_image_url']
                print('images: ', images)
            except (KeyError, TypeError, IndexError):
                images = None
                print('images: ', images)

            try:
                page_categories = node['collated_results'][0]['snapshot']['page_categories']
                page_categories = ', '.join(page_categories)
                print('page_categories: ', page_categories)
            except (KeyError, TypeError):
                page_categories = None
                print('page_categories: ', page_categories)

            try:
                video_sd_url = node['collated_results'][0]['snapshot']['videos'][0]['video_sd_url']
                print('video_sd_url: ', video_sd_url)
            except (KeyError, TypeError, IndexError):
                video_sd_url = None
                print('video_sd_url: ', video_sd_url)

            try:
                start_date = node['collated_results'][0]['start_date']
                # print('start_date (raw): ', start_date)
                
                if isinstance(start_date, int):
                    readable_date = datetime.datetime.fromtimestamp(start_date).strftime('%Y-%m-%d')
                    print('start_date: ', readable_date)
                else:
                    readable_date = None
                    print('start_date is not a valid timestamp')
            except (KeyError, TypeError):
                readable_date = None
                print('start_date: ', readable_date)


            if body and body.strip() == "{{product.brand}}":
                try:
                    body = node['collated_results'][0]['snapshot']['cards'][0]['body']
                    body = ' '.join(body.split())
                    body = body.strip()
                    print('body: ', body)
                except (KeyError, TypeError, IndexError):
                    body = None
                    print('body: ', body)

                try:
                    link_description = node['collated_results'][0]['snapshot']['cards'][0]['link_description']
                    print('link_description: ', link_description)
                except (KeyError, TypeError, IndexError):
                    link_description = None
                    print('link_description: ', link_description)

                try:
                    link_description = node['collated_results'][0]['snapshot']['cards'][0]['link_description']
                    print('link_description: ', link_description)
                except (KeyError, TypeError, IndexError):
                    link_description = None
                    print('link_description: ', link_description)

                try:
                    title = node['collated_results'][0]['snapshot']['cards'][0]['title']
                    print('title: ', title)
                except (KeyError, TypeError, IndexError):
                    title = None
                    print('title: ', title)

        
            Ads.objects.get_or_create(
                ad_archive_id=ad_archive_id,
                defaults={
                    'page_name': page_name,
                    'title': title,
                    'body': body,
                    'caption': caption,
                    'link_description': link_description,
                    'link_url': link_url,
                    'images': images,
                    'page_categories': page_categories,
                    'video_sd_url': video_sd_url,
                    'start_date': readable_date,
                    'collation_id': collation_id,
                    'page_id': page_id
                }
            )


            print()
            print('-' * 50)
            print()

        previous_cursor = None
        try:
            next_cursor = response_json['data']['ad_library_main']['search_results_connection']['page_info']['end_cursor']
            if not next_cursor or next_cursor == previous_cursor:
                print("No new cursor found or cursor is the same. Stopping.")
                break
            print('next_cursor: ', next_cursor)
        except (KeyError, TypeError):
            next_cursor = None
            print('next_cursor: ', next_cursor)

        if next_cursor:
            variables = json.loads(payload['variables'])
            variables['cursor'] = next_cursor
            payload['variables'] = json.dumps(variables)
        else:
            print("Cursor not found, stopping.")
            break  

    except json.JSONDecodeError:
        print("Response is not valid JSON. Saving as plain text.")
        with open("facebook_graphql_response.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("Response saved to facebook_graphql_response.html")

