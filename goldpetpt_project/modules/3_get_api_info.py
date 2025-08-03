from load_django import *
from parser_app.models import *
import requests
import json
from bs4 import BeautifulSoup

# url = "https://goldpet.pt/index.php?controller=product&token=d41d8cd98f00b204e9800998ecf8427e&id_product=31566&id_customization=0&id_product_attribute=36797&group%5B4%5D=394&group%5B3%5D=39&qty=1"

# headers = {
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     # "accept-encoding": "gzip, deflate, br, zstd",
#     "accept-language": "ru,en-US;q=0.9,en;q=0.8",
#     "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
#     # "cookie": "PHPSESSID=n2ikf4t64dlnmjakd1oput96in; GOLDPET-591644096bab2e34fc10f55e54f9f16d=def50200375c88cdc171675fae0327f76229247f6aa1fb34d941452cf5fead30974e0254d259ed8a65aebd12ce2c621bf7c52f9e934c2c00c6ad815e4fdcfcc8114b8f54b3ce53676fa150c6a86a29c4a36a9ca087817dc53ae180441b9cb876046d2c9615edbada485fb19d3ebcc77079b42467d02c5017fca5aed0b8c3a362f4c4599a65d5ed0a62e64c432329935ddc449ffc968baa2619e3f83af98b27100e9829db965a2397aaf3c69558a54c28dc99a5cafa785b6567c30d555299c6bf43449333c0f0bbbfb481a9fc47b7471a2fa91f695586fad932; _ga=GA1.1.527396355.1734680240; fbp=fb.1.1734680240.tR0c4XdJtfez; _gcl_au=1.1.2019759290.1734680244; _fbp=fb.1.1734680244901.858484306168492010; external_id=0; GOLDPET-932abc651341b1852078841aa600665b=def5020073a358ef4ae29866c44496552aa88d05205a57f0a0265c988a17779d830507d5a836a243c606d78c19a2157e1f99c295b3ce08daa723210faf68b2cb22eae05e398b749a3f53da43a812954a64ec70853443c01caf12c6460f88ecc778f2df91c5a45bd280f839c57f3b6b143192794c01e3d23641da1c910fd9354c8d6d8010fb22526e48c7662762f289c75f3e16c601cd7885dc08afa13b234167c13ecc16de6e7c47f6e98be9d06620de50f8cbba27ddd17a95a9107eef792c06c2a252d9cb6f26d6f3c4bffabdae664ded2868fd32e9f961d0ebfc2d7c42675e71b6b32f18ecd537bc311c5cf01e892e3a961a476d98e1df61750c58fb97b46e69efdc70c815a69095a57656721d11566246fea86ef073f778ce659209fbc69df06860a8830f359d5ba0354296c66ccab0ea24ffdc93aeb8ae14661a5b",
#     "cookie": "cf_clearance=fX22yYz9fkXP6pcI9bIt5W8NYK7aQaiCBsy6q75ZYr8-1734979556-1.2.1.1-Xyk.NuHYy8LyEaL.lBXMh1Zw8bARBup.6rKr5kYsc6ZECpaeY2V9eAIZLFwqrxEZ1KvjiUf5KVt2NkYVvjq1pW0ifeaI0pYbEM8je6s5Z1lj5v82RBCh4W1dEO_PNvrub7hfNBTNFNURNp5ZIrxZATpIKPZd8QVDaDOE2Tu2C1xktu6oxcNVIRQ.u6GrVtnzlDdBpfpMGBSK1nA6A.SQ0pfDbjbYkRufVMGKuH7qCf0KZvec955aWq4j4qAWRevlcXqh7m4ctcM1aMI5SFHnV6zB.0B2SRQz7XKIvag90qrXYhwKTqXk1uHoB0snwmXOpd_xrxtUQ2RRy61IxEW8OY4UqybxVMtLyWllNSgJzfBPKsYI9bowsZNc.0TZkKzVR3NFLpb4FqT5jNMembJh.JcwFRxT2WDGFbtme3BbaCVw.p4vr1hfW1nI9bwZMajH; PHPSESSID=8g8lj421ocfmqrver4bhq875tm; GOLDPET-591644096bab2e34fc10f55e54f9f16d=def50200948c8cf1ee7b55067a6d02fee3d588f6f8c4937e5e08c2d927e91447652ff65ca308aed4393de78b8e1acfe02cd6e753e6d5b8defa76168124e9cb4d2d8fe96233853c9c31206789c4a17c49abd3099afc76cf0af7882e68cabb4e4505081b47ee7a960d3807b2f225b8dd9817c3eebfb139c60fac822d4c348136f4aef89bab0714a4cbf6dbb39bc442ed4dd01340eecb925425d7d715a0a3047931bbebda0649cf981556087dad38aeb2d74e3f8ae24b13b064ed8bb387373366a88b4040372940c087466211d1a66ff30a716c3d2dd08c77c235; _ga=GA1.1.1154117056.1734979564; fbp=fb.1.1734979564.NhTXt0LQ2Cj2; _gcl_au=1.1.1140929010.1734979565; _fbp=fb.1.1734979565126.727085030178121259; GOLDPET-932abc651341b1852078841aa600665b=def5020081556dc41f272721acb0f2ffd9faddaf5effaed5a6a202f01f9acb6095f40e02596d9fbf113300df19440148c0c090c7d0540f738bd3c6f120a352a8bf2679199c8de43070a6dc3db56da1ed3c0b5a07bac18efaa7bf5e4d33c04e4f8cf43be3dcb603d7bdd8d73fa53c97043e584d8d6d99c5506cc5080bc5789c78a6ef99229e5fd10ada80766cd2b855ca642cb48ad4b81772f5b9fa26517547863e65e55e1d7648dc73dd51c19db316a573fc81bf4841831ceee74dbfdf325c772a4be143de7e6b0f74d860215ef231e94b8bd78788fbe5b4454cb8fb62a5ac74c78ac2a9cfd9fe6214d0e7ce0f48b599af3266bcd5ed194b4c0e829457b617e47b4749da4dff33294faf818630a20c57d057ead71ff9d967e8983c1f1853c672bdb19b1ad0e5a890adaa5b61ad0106a15d9c489389987c4f2ff2fcf65b; _ga_PD390SHGE4=GS1.1.1734979564.1.0.1734979577.47.0.190000792",
#     "origin": "https://goldpet.pt",
#     "referer": "https://goldpet.pt/capas-e-casacos/31566-36797-casaco-caldoso-azul-para-caes-ferribiella.html",
#     "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Windows"',
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "x-requested-with": "XMLHttpRequest"
# }
# url = "https://goldpet.pt/index.php?controller=product&token=d41d8cd98f00b204e9800998ecf8427e&id_product=31623&id_customization=0&id_product_attribute=37038&group%5B4%5D=138&group%5B3%5D=39&qty=1"

# # Заголовки запроса
# headers = {
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     # "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Cookie": "PHPSESSID=d9a7bn4av4nimcre0pd3km8i17; GOLDPET-591644096bab2e34fc10f55e54f9f16d=def502006b9f7f3f56824a16a510ad0a082c225ca0cae6c0723cf4d766ac114954bae8ee7e3fadbedb393a683b3c219f4f83f6b4b359ec3af6e36f0340495865c7c56de80da93af8b77b73329dcee9bf2a9973468ec4ba765111143ddfb07b76475fd7be1bb476b1f6b11418f7274d6301229723c66c6105de7911775b295a02fdea7a3891b78e916badc21c5850b9d2426a80d15824956860656871faa212676f46e0b7f056fea76563cc918d9b7ebbb1febc56ee4bad0d555d186ea4be7870c6c78cea8f0b8a550eb4f2de3fa33ac8ec4171c507ccf9badf; _ga=GA1.1.2064008494.1734980030; fbp=fb.1.1734980029.eMNv2gwjjqoU; _gcl_au=1.1.303922416.1734980030; _fbp=fb.1.1734980030171.725073508480287824; GOLDPET-932abc651341b1852078841aa600665b=def5020080c39952ec273d3b0cfccb0d1c5976d6143c07435f978da304772b6c834dc87ff943ca4c86ae467fe2d354d6a7e7a4358c54892873a83d2835ffc5b6a89d24e7ab2a3590a700c75c15c9cf7ca530ddc0eeba511397ea1a0636b5fa2fc2a412aa63256de4de1caca70a06fa65677aefd9b87fa3daa320dd7d2cd1e3666edde9f25a80c19daa41239714d1de622a773f4b1f22b1d77db8d01db87ec46959a8b229046f27c1a5bb32ff7a6343d8c4174298bc78bc4c2cd4b7264da69944f95470dd76cc6b9d2c303616bc9348242098e3a8250ce1c5ea37f9c7548b837877bc39447ff33cc664daf2958a020ae0e3b4ce66cac0895991744e9d178e3569a2601f02d2e5cdb4ab1444d16d52b6f6015bdb2a179bffe82e4c3eff9c99ebc4b6100d6bc40a7553483325af357e569f1cf35f82857a36fa858dd12d65; _ga_PD390SHGE4=GS1.1.1734980029.1.1.1734980058.31.0.645043503",
#     "Origin": "https://goldpet.pt",
#     "Referer": "https://goldpet.pt/camisolas/31623-37038-camisola-polarotto-azul-para-caes-ferribiella.html",
#     "Sec-Ch-Ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": '"Windows"',
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#     "X-Requested-With": "XMLHttpRequest"
# }
# URL для запроса
url = "https://goldpet.pt/index.php"

# Заголовки запроса
headers = {
    "authority": "goldpet.pt",
    "method": "POST",
    "path": "/index.php?controller=product&token=d41d8cd98f00b204e9800998ecf8427e&id_product=31623&id_customization=0&id_product_attribute=37039&group%5B4%5D=188&group%5B3%5D=39&qty=1",
    "scheme": "https",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "cookie": "cf_clearance=sUVIC1A5Sl9lXJhvlelze3ArhoSg.pXtZ5hzbPN1Lg4-1734980560-1.2.1.1-N2ujEIiGdWt3aXsbJkfZGFrHO18gMVosG2KXYGpGPE22GWCJfxhgW1nCdE0dJjsHyw7KKiGMub3CwQMcBZMvNk90pVFSqF4xr9TtHis3rKSj07_GTm2oZCneYBdppQr5_ung8xMx1NbNeluIYK.FdzGoFkQKYrXtvSdpMeCwqqSP9vxAVxkkFNu.B9QmUH72mXDdW0mosbtJE6bk.Z8E4dc7QQFJf1aTqfDENKbEabmw_41TtRCuA9LKZS8y0dO1BuX6DZNK4Tri_gfsYdOwGF1FPFTJtNxJFJwCZnIRskVio43Xt7L4eZQC5kQuMiSoJLUJ2pALYPOlqddICGtDA090avMiVsp80RGz.TvRTTaaihEbUK.tgbHo_Qk3D6I2oErvEunoRLLQcA3UkzyESfebilSjiSNFL_qa5l3ULL9OCalCXWDz5wjOIdyhup8Y; PHPSESSID=78lvug8j1pgrg6qfe87h0v8qtf; GOLDPET-591644096bab2e34fc10f55e54f9f16d=def502006ff1e924325c5d7d482e978ca5bea23a75054d4f59fb403f84eb2c566cb4c57883cf2a57c98d183a4b5a1afd211f4f118e7bf47c787d3be1eb1d12afcd258bf15b0e36a1ef407c829385be584abaef4910d92067cc5fd9a0524d2a123ebf6f051eb9f58657d7ffc0f19c62fab1deaa8cbff0c5e6e2dace40c4a169ddb3bb4ee939687333f5eed31ccc32f69bbaffdb106268cd6b8b76192058a0ecfcd83f891c05078f0de4fc01249239beb7be07e38dacea3cf555dc5cf0ce42908da32a1f0d013e1500bbffe471567c38186df5f82b996060f947; _ga=GA1.1.602895918.1734980568; fbp=fb.1.1734980567.QGsvXK58NzXs; _gcl_au=1.1.686541161.1734980568; _fbp=fb.1.1734980568105.10012713336609932; GOLDPET-932abc651341b1852078841aa600665b=def502001f8a4416a5ee03e19ad686e0bb43c82ac8d32eb55e34579cf640ed7383331d3a67014c5b740d0f09b17869cbea8e7ad66c8b21944ca4c0cfcc8cd4a3d9936640ebab0aeab90890828db3a5c4d071b441411325f1f34cab13e4b1d0601f8b0dab27d3209177ae845dd55e83ef85c452e966820c03b8addcfa0110f13828e6b90855665a55729e67774d2e4e2fe61c25b4130d12d54c8bbfbf4337101920f4513884c660c2b852ad80444fa4fea025310ee7c83ad3f8af23a5473f22488ec8f8f64f9213be50cc47fa77ebfb55ab27408f2f007d278fb29ab427f7150c66f34470294b48cc0ec8378662b3e57e56ad28b56b3cd5d41525cc99922c7680399662af7be58462fe750b6f47d82b1d4224dd506d677eb4690db26158dabc0b67b7b21ed1ea042f7c01727a3d54ebe2c7d3e0718f4b27a1c0ce76fd31; _ga_PD390SHGE4=GS1.1.1734980567.1.0.1734980579.48.0.1349689005",
    "cookie": "PHPSESSID=3f7gb66rg3vbrgc68r08gmvqmk; GOLDPET-591644096bab2e34fc10f55e54f9f16d=def502006d13af3154d32cd535bd4faaf32f860061a2f7d6ad51193e8800b9e1ee12a467e35732e3b8925ded9c6d5ecf521f750f612490628514ed46961bbcb778d3553cfc1597ed7b2ac96b3f5970d1f75a4f0b53011fb83fcf44f05ca54055f3c96c4af1e7c17f7ae44366fa4d48720230222f5916f79b020fb5396cb1faf86fba30e0530b7194cf1b96d8388300d3727cc21d71196ce40f3ef83612ddcb155c09b48bbe5a6a08b3cc3021309ce0c6a77cd6a85d0c0dff9fe788a0728c4c23efb6bf3e0249006e0351758d00af36826f3e3790331943d051; _ga=GA1.1.1813840447.1735023683; fbp=fb.1.1735023681.Qi5dY1vVG9Rs; _gcl_au=1.1.1155913311.1735023683; _fbp=fb.1.1735023683413.34945189177101541; GOLDPET-932abc651341b1852078841aa600665b=def50200ee5cb780a42074a2198619dbab4a5ceeed28cf9d9428c922b4c0d5c0f9fdad6bf80227525cfbafca570ad050f65a190fc9906c3582776756912d4a19687547409e8d9ce4a718d4ab27078d3614062abbfb82eb588f348d1ff5365f35176b677e204c385518673fa22715d0ed63a6ec015cfacbaa52979754c7056f4c90cfd875b15794576dd2cc77c107bf64afddf61e73b5e989f9e2fca3e4e483ad0e305582febcd6a1f75b0c7da04940b49ea2eb0ffd52e5a5d5a4214cbf0d636296095d2caa589ed3a15e4b0c2e77d16f59adb1802f8f82c5b43b95276b4523e3d24847146d44555264742a39fdbd17f335da729dd638239e96dcb6e00843bc78cf8113d39c02e474d5cbf70fb0bb2bccddc07c6461ae94007c2ba11fd232a16698e3aec7979957477da35e74e5db0451d8263acb7947ebd9ce542905c7; _ga_PD390SHGE4=GS1.1.1735023683.1.0.1735023699.44.0.540288157",
    "origin": "https://goldpet.pt",
    "referer": "https://goldpet.pt/camisolas/31623-37039-camisola-polarotto-azul-para-caes-ferribiella.html",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

# for item in Product.objects.order_by("id")[7065:]:
for item in Product.objects.filter(status="New").order_by("id"):
    print(item.id)
    print()

    payload = {
        "controller": "product",
        "token": "d41d8cd98f00b204e9800998ecf8427e",
        "id_product": f"{item.id_product}",
        "id_customization": "0",
        # "id_product_attribute": "36797",
        f"{item.name_variants}": f"{item.value}",
        # f"group[8]": f"534",
        # "group[3]": "39",
        "qty": "1",
        "quickview": "0",
        "ajax": "1",
        "action": "refresh",
        "quantity_wanted": "1"
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        print("Request successful!")
        # print(response.json())
        data = response.json()
        # with open('files/3_get_api_info_1.json', 'w') as f:
        #     json.dump(data, f, indent=4)
        soup = BeautifulSoup(response.text, "html.parser")

        product_prices = data['product_prices']
        soup_product_prices = BeautifulSoup(product_prices, "html.parser")

        
        # try:
        #     main_category = soup.find("span", itemprop="name", string=f"{item.category_main}")
        #     next_category = main_category.find_parent("li").find_next_sibling("li")
        #     category_sub = next_category.find("span", itemprop="name").text if next_category else None
        # except Exception as e:
        #     category_sub = None
        #     print("Error: ", e)

        # print("all_category: ", category_sub)

        try:
            price = soup_product_prices.find("span", itemprop="price").text
        except Exception:
            price = None
        print("price: ", price)

        try:
            regular_price_amount = soup_product_prices.find("span", class_="regular-price").text
        except Exception:
            regular_price_amount = None
        print("regular_price_amount: ", regular_price_amount)

        try:
            discount_percentage_absolute = soup_product_prices.find("span", class_="discount-percentage").text
        except Exception:
            discount_percentage_absolute = None
        print("discount_percentage_absolute: ", discount_percentage_absolute)

        
        product_details = data['product_details']
        soup_product_details = BeautifulSoup(product_details, "html.parser")

        try:
            ean13 = soup_product_details.find("dt", string="ean13").find_next_sibling().text
        except Exception:
            ean13 = None
        print("ean13: ", ean13)
        
        try:
            upc = soup_product_details.find("dt", string="upc").find_next_sibling().text
        except Exception:
            upc = None
        print("upc: ", upc)

        try:
            ref_span = soup_product_prices.find('div', class_='product-reference').find('span', class_='control-label')
            ref_number = ref_span.text.strip().replace('Ref: ', '')
        except Exception:
            ref_number = None
            # Выводим результат
        print("Ref:", ref_number)

        try:
            brand_logo = soup_product_details.find("img", class_="manufacturer-logo")
            if brand_logo:
                brand_name = brand_logo["alt"]
            brand_logo = brand_logo["src"]
        except Exception:
            brand_logo = None
        print("brand_logo: ", brand_logo)
        print("brand_name: ", brand_name)

        print()

        item.price = price
        item.regular_price_amount = regular_price_amount
        item.discount_percentage_absolute = discount_percentage_absolute
        item.ean13 = ean13
        item.upc = upc
        item.brand_name = brand_name
        item.brand_logo = brand_logo
        item.ref_number = ref_number
        # item.category_sub = category_sub
        item.status = "Done"
        item.save()

    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
