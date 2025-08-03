from load_django import *
from parser_app.models import *
import os
import requests
import ast

def download_images():
    items = Product.objects.filter(status="Done").order_by("id")  # Берем продукты со статусом "New"

    for item in items:
        try:
            # Преобразуем поле `image_links` в список
            raw_image_links = item.image_links.replace("'", '"')  # Заменяем одинарные кавычки
            try:
                urls = ast.literal_eval(raw_image_links)  # Преобразуем строку в список
                if not isinstance(urls, list):  # Если это не список, оборачиваем в список
                    urls = [urls]
            except Exception as e:
                print(f"Ошибка преобразования image_links для item.id={item.id}: {e}")
                continue

            # Формируем папку для сохранения
            save_folder = f"results/images/{item.brand_name or 'unknown'}"
            os.makedirs(save_folder, exist_ok=True)

            # for i, url in enumerate(urls):  # Обрабатываем каждую ссылку
            #     # Определяем имя файла
            #     if item.ean13:
            #         filename = f"{item.ean13}_{i + 1}.jpg"  # Добавляем индекс для уникальности
            #     else:
            #         filename = f"{item.ref_number}_{i + 1}.jpg"

            for i, url in enumerate(urls):  # Обрабатываем каждую ссылку
    # Определяем имя файла
                if item.ean13:
                    if i == 0:
                        filename = f"{item.ean13}.jpg"  # Для первой картинки без суффикса
                    else:
                        filename = f"{item.ean13}({i}).jpg"  # Для остальных с суффиксом в скобках
                else:
                    if i == 0:
                        filename = f"{item.ref_number}.jpg"
                    else:
                        filename = f"{item.ref_number}({i}).jpg"
                filepath = os.path.join(save_folder, filename)

                # Скачиваем изображение
                response = requests.get(url)
                if response.status_code == 200:
                    with open(filepath, "wb") as file:
                        file.write(response.content)
                    print(f"Изображение сохранено: {filepath}")
                else:
                    print(f"Ошибка при скачивании {url}. Статус-код: {response.status_code}")

            # Обновляем статус продукта
            item.status = "Done1"
            item.save()
            print(f"Статус продукта с ID {item.id} обновлен на 'Done'.")

        except Exception as e:
            print(f"Ошибка при обработке продукта {item.id}: {e}")

if __name__ == "__main__":
    download_images()
