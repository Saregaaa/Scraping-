from load_django import *
from parser_app.models import *
import os
import requests
import ast
from concurrent import futures


def process_item(item):
    """Обрабатывает один элемент Product."""
    try:
        # Преобразуем поле `image_links` в список
        raw_image_links = item.image_links.replace("'", '"')  # Заменяем одинарные кавычки
        try:
            urls = ast.literal_eval(raw_image_links)  # Преобразуем строку в список
            if not isinstance(urls, list):  # Если это не список, оборачиваем в список
                urls = [urls]
        except Exception as e:
            print(f"Ошибка преобразования image_links для item.id={item.id}: {e}")
            return

        # Формируем папку для сохранения
        save_folder = f"results/images/{item.brand_name or 'unknown'}"
        os.makedirs(save_folder, exist_ok=True)

        for i, url in enumerate(urls):  # Обрабатываем каждую ссылку
            # Определяем имя файла
            if item.ean13:
                filename = f"{item.ean13}.jpg" if i == 0 else f"{item.ean13}({i}).jpg"
            else:
                filename = f"{item.ref_number}.jpg" if i == 0 else f"{item.ref_number}({i}).jpg"
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
        print(f"Статус продукта с ID {item.id} обновлен на 'Done1'.")

    except Exception as e:
        print(f"Ошибка при обработке продукта {item.id}: {e}")


if __name__ == "__main__":
    # Получаем список продуктов для обработки
    items = Product.objects.filter(status="Done").order_by("id")

    # Используем многопоточность для обработки
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_item, items)
