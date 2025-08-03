from load_django import *
from parser_app.models import *
import requests
from bs4 import BeautifulSoup


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Cookie": "PHPSESSID=d9a7bn4av4nimcre0pd3km8i17; GOLDPET-591644096bab2e34fc10f55e54f9f16d=def502006b9f7f3f56824a16a510ad0a082c225ca0cae6c0723cf4d766ac114954bae8ee7e3fadbedb393a683b3c219f4f83f6b4b359ec3af6e36f0340495865c7c56de80da93af8b77b73329dcee9bf2a9973468ec4ba765111143ddfb07b76475fd7be1bb476b1f6b11418f7274d6301229723c66c6105de7911775b295a02fdea7a3891b78e916badc21c5850b9d2426a80d15824956860656871faa212676f46e0b7f056fea76563cc918d9b7ebbb1febc56ee4bad0d555d186ea4be7870c6c78cea8f0b8a550eb4f2de3fa33ac8ec4171c507ccf9badf; _ga=GA1.1.2064008494.1734980030; fbp=fb.1.1734980029.eMNv2gwjjqoU; _gcl_au=1.1.303922416.1734980030; _fbp=fb.1.1734980030171.725073508480287824; GOLDPET-932abc651341b1852078841aa600665b=def5020080c39952ec273d3b0cfccb0d1c5976d6143c07435f978da304772b6c834dc87ff943ca4c86ae467fe2d354d6a7e7a4358c54892873a83d2835ffc5b6a89d24e7ab2a3590a700c75c15c9cf7ca530ddc0eeba511397ea1a0636b5fa2fc2a412aa63256de4de1caca70a06fa65677aefd9b87fa3daa320dd7d2cd1e3666edde9f25a80c19daa41239714d1de622a773f4b1f22b1d77db8d01db87ec46959a8b229046f27c1a5bb32ff7a6343d8c4174298bc78bc4c2cd4b7264da69944f95470dd76cc6b9d2c303616bc9348242098e3a8250ce1c5ea37f9c7548b837877bc39447ff33cc664daf2958a020ae0e3b4ce66cac0895991744e9d178e3569a2601f02d2e5cdb4ab1444d16d52b6f6015bdb2a179bffe82e4c3eff9c99ebc4b6100d6bc40a7553483325af357e569f1cf35f82857a36fa858dd12d65; _ga_PD390SHGE4=GS1.1.1734980029.1.1.1734980058.31.0.645043503",
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

for item in Product.objects.filter(status="Done1").order_by("id"):

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
