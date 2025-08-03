from load_django import *
from parser_app.models import *
import csv

def extract_zip_codes(file_path):
    zip_codes = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            zip_codes.append(row['ZIP Code'])
    return zip_codes

# Использование
file_path = 'us_zipcodes.csv'
zip_codes = extract_zip_codes(file_path)

for code in zip_codes:
    print(code)

    ZipCode.objects.get_or_create(zip_code=code)

