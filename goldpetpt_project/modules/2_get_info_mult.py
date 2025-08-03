from load_django import *
from parser_app.models import *
import requests
from bs4 import BeautifulSoup
from concurrent import futures

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Cookie": "external_id=0; PHPSESSID=rh888d5e6br8bhvh2rgj40kb7u; GOLDPET-591644096bab2e34fc10f55e54f9f16d=def502004748b5bd2e69bc460680cd911deb8af9fffc21f8968b07638e12e5c1b43b06da54c8b3aa02078797b91cb8624c67f91beef6144708dc3f152b1ab0d6eec20db3db9fec4a79c3760ce994864bae06596aad36efa4e7eae9f31382a91a4101dad589ed24a683c520c5700f603d6942639f2d47181e51c1ed82f7692a474d3569224e5928325f1cbe596d556281cba2a120e138b1f04732f7b693b3c5c20a42c356186f5afbc487541b94cf060b0e91f20e102a0fce530cdd2d13128f197d71a92c38d0e014bb5e8a85f59ba45a96f02f8ef4f28a5c2f; _ga=GA1.1.2136411844.1734972881; _gcl_au=1.1.1006311442.1734972881; fbp=fb.1.1734972882.1zeOXC1L43HL; _fbp=fb.1.1734972883434.265634300816218784; GOLDPET-932abc651341b1852078841aa600665b=def502008b72dac8b85a2cc6ed6834e1deb7bec16ffcb1900a631f29779799d7e96561e6ad35dcd433f8b64afd450ac6f8d97291323324d4a49db3627440a427fd409c4ec057410586280e2b2cc3a79748210ae7f2e8289c645baf212656b0d0c95ccbda0fe1efc00ba0a3939f63623ec1d71422d94052fe6f952d89aa5dd66172750394ea9aa05de02acae151cbf2cda23004b3246fc5b41c94c1b17382f8ef5545a593c8656a5f7a1c19d639f24cb4f592bbab675a0e63baece196b2698ad5c1e0acc6b851930fa0f7958a10b6b467237758425602e561332666a9e3786ddffd90535e46d4ff93bf7c9b045baf95a0f3e72db64990642c3bffc27762d76777498dd62f2a2751c3f152716730df3a091fd0f6e76eb7a44efa4556415e34a6799c379d1f924c7b1ff6e3781b62ebc87e1e736332841c0057318bd5; _ga_PD390SHGE4=GS1.1.1734972880.1.1.1734972950.60.0.824058806",
    "Referer": "https://goldpet.pt/3-cao",
    "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

def main(item):
# for item in Product.objects.filter(status="Done").order_by("id"):

    print()
    print("Item: ", item.id)
    print()

    url = item.link
    # url = "https://goldpet.pt/racao-seca/19010-16715-royal-canin-exigent-mini-adult-racao-seca-para-cao-de-porte-pequeno-com-apetite-exigente.html"
   
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Success!")
        # print(response.text)  

        soup = BeautifulSoup(response.text, "html.parser")
        
        try:
            main_category = soup.find("span", itemprop="name", string=f"{item.category_main}")
            next_category = main_category.find_parent("li").find_next_sibling("li")
            category_sub = next_category.find("span", itemprop="name").text if next_category else None
        except Exception as e:
            category_sub = None
            print("Error: ", e)

        print("all_category: ", category_sub)

        try:
            product_description = soup.find("div", id="description").text
            # prouct_description = prouct_description.replace("\n", " ")
            product_description = " ".join(product_description.split())
        except Exception:
            product_description = None
        print("prouct_description: ", product_description)
      

        description_div = soup.find("div", itemprop="description")

        if description_div:
            brief_description = ""  # Строка для объединения текстов
            paragraphs = description_div.find_all("p")
            for p in paragraphs:
                brief_description += p.text.strip().replace("\n", " ") + " "
            print("Brief description:", brief_description.strip())
        else:
            print("No description found.")


        try:
            quantidade = soup.find("span", string="Quantidade").find_next_sibling().text.strip()
            quantidade = quantidade.replace("\n", " ")
        except Exception:
            quantidade = None
        print("Quantidade: ", quantidade)

        try:
            brand_logo = soup.find("img", class_="manufacturer-logo")
            if brand_logo:
                brand_name = brand_logo["alt"]
            brand_logo = brand_logo["src"]
        except Exception:
            brand_logo = None
        print("brand_logo: ", brand_logo)
        print("brand_name: ", brand_name)

        try:
            ean13 = soup.find("dt", string="ean13").find_next_sibling().text
        except Exception:
            ean13 = None
        print("ean13: ", ean13)
        
        try:
            upc = soup.find("dt", string="upc").find_next_sibling().text
        except Exception:
            upc = None
        print("upc: ", upc)

        data_sheet = soup.find('dl', class_='data-sheet')
        data = {}
        if data_sheet:
            for dt, dd in zip(data_sheet.find_all('dt', class_='name'), data_sheet.find_all('dd', class_='value')):
                key = dt.get_text(strip=True)
                value = dd.get_text(separator=' ', strip=True)  # Добавлен separator=' '
                data[key] = value

        animal = data.get('Animal', '')
        idade = data.get('Idade', '')
        porte = data.get('Porte', '')
        caracteristicas = data.get('Características', '')
        alimento = data.get('Alimento', '')
        gama = data.get('Gama', '')
        proteina_sabor = data.get('Proteína/sabor', '')
        tipo_produto = data.get('Tipo de produto', '')

        print("Animal:", animal)
        print("Idade:", idade)
        print("Porte:", porte)
        print("Alimento:", alimento)
        print("Gama:", gama)
        print("Proteína/sabor:", proteina_sabor)
        print("Tipo de produto:", tipo_produto)

        try:   
            carousel = soup.find("ul", class_="product-images")    
            if carousel:
                images = carousel.find_all("img")
                image_links = [img['src'] for img in images if 'src' in img.attrs]
            else:
                image_links = []        
        except Exception as e:
            print("Error: ", e)
            image_links = []
        print("Image links:", image_links)


        try:
            price = soup.find("span", itemprop="price").text
        except Exception:
            price = None
        print("price: ", price)

        try:
            regular_price_amount = soup.find("span", class_="regular-price").text
        except Exception:
            regular_price_amount = None
        print("regular_price_amount: ", regular_price_amount)

        try:
            discount_percentage_absolute = soup.find("span", class_="discount-percentage").text
        except Exception:
            discount_percentage_absolute = None
        print("discount_percentage_absolute: ", discount_percentage_absolute)

        try:
            ref_span = soup.find('div', class_='product-reference').find('span', class_='control-label')
            ref_number = ref_span.text.strip().replace('Ref: ', '')
        except Exception:
            ref_number = None
            # Выводим результат
        print("Ref:", ref_number)

        # product_variants = soup.find("div", class_="product-variants-item")
        product_variants = soup.find("div", class_="product-variants")
        try:
            inputs = product_variants.find_all('input', class_='input-radio')
        except Exception as e:
            inputs = None     
        print("inputs: ", inputs)

        # Извлекаем необходимые атрибуты
        data = []
        if inputs:
            for input_tag in inputs:
                data_product_attribute = input_tag.get('data-product-attribute')
                name = input_tag.get('name')
                value = input_tag.get('value')
                title = input_tag.get('title')
                data.append({
                    'data_product_attribute': data_product_attribute,
                    'name': name,
                    'value': value,
                    'title': title
                })
        if data:
            # Вывод результатов
            for i in data:
                # data_product_attribute = i['data_product_attribute']
                name_variants = i['name']
                value = i['value']
                product_variation = i['title']

                if data:
                    item.product_variation = data[0].get('title', None)
                else:
                    item.product_variation = None
                if data:
                    item.name_variants = data[0].get('name', None)
                else:
                    item.name_variants = None
                if data:
                    item.value = data[0].get('value', None)
                else:
                    item.value = None
                item.save()

                # try:
                #     Product.objects.filter(
                #         name_variants=name_variants,
                #         value=value,
                #         product_variation=product_variation,
                #         id_product=item.id_product  # дополнительное условие
                #     ).update(category_sub=category_sub)
                # except Exception as e:
                #     print("Error: ", e)
                #     continue

                try:
                    Product.objects.get_or_create(
                        # data_product_attribute=data_product_attribute,
                        name = name,
                        name_variants=name_variants,
                        value=value,
                        product_variation=product_variation,
                        defaults={
                            "id_product": item.id_product,
                            "name": item.name,
                            "description_short": item.description_short,
                            "category_name": item.category_name,
                            "category_main": item.category_main,
                            "image": item.image,
                            "brand_name": item.brand_name,
                            "brand_logo": item.brand_logo,

                            "category_sub": category_sub,
                            "product_description": product_description,
                            "brief_description": brief_description,
                            "quantidade": quantidade,
                            "animal": animal,
                            "idade": idade,
                            "porte": porte,
                            "caracteristicas": caracteristicas,
                            "alimento": alimento,
                            "gama": gama,
                            "proteina_sabor": proteina_sabor,
                            "tipo_produto": tipo_produto,
                            "image_links": image_links,
                        }
                    )
                except Exception as e:
                    print("Error: ", e)
                    continue

        item.product_description = product_description
        item.brief_description = brief_description
        item.quantidade = quantidade
        item.brand_logo = brand_logo
        item.ean13 = ean13
        item.upc = upc
        item.animal = animal
        item.idade = idade
        item.porte = porte
        item.caracteristicas = caracteristicas
        item.alimento = alimento
        item.gama = gama
        item.proteina_sabor = proteina_sabor
        item.tipo_produto = tipo_produto
        item.image_links = image_links
        item.brand_name = brand_name
        item.discount_percentage_absolute = discount_percentage_absolute
        item.regular_price_amount = regular_price_amount
        item.ref_number = ref_number
        # item.product_variation = product_variation
        item.category_sub = category_sub
        item.status = "Done"
        item.save()


    else:
        print(f"Error: {response.status_code}")

items = Product.objects.filter(status="Done1").order_by('id') 

with futures.ThreadPoolExecutor(30) as executor:
    executor.map(main, items)