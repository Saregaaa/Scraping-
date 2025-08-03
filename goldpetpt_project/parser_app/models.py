from django.db import models

# Create your models here.



class Product(models.Model):
    id_product = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    discount_percentage_absolute = models.CharField(max_length=100, blank=True, null=True)
    regular_price_amount = models.CharField(max_length=100, blank=True, null=True)
    description_short = models.TextField(blank=True, null=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    category_sub = models.CharField(max_length=255, blank=True, null=True)
    category_main = models.CharField(max_length=255, blank=True, null=True)

    product_description = models.TextField(blank=True, null=True)
    brief_description = models.TextField(blank=True, null=True)
    ean13 = models.CharField(max_length=100, blank=True, null=True)
    upc = models.CharField(max_length=100, blank=True, null=True)
    product_variation = models.CharField(max_length=200, blank=True, null=True)
    quantidade = models.CharField(max_length=300, blank=True, null=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    brand_logo = models.CharField(max_length=500, blank=True, null=True)
    animal = models.CharField(max_length=500, blank=True, null=True)
    idade = models.CharField(max_length=200, blank=True, null=True)
    porte = models.CharField(max_length=200, blank=True, null=True)
    caracteristicas = models.CharField(max_length=200, blank=True, null=True)
    alimento = models.CharField(max_length=200, blank=True, null=True)
    gama = models.CharField(max_length=200, blank=True, null=True)
    proteina_sabor = models.CharField(max_length=200, blank=True, null=True)
    tipo_produto = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    image_links = models.TextField(blank=True, null=True)
    # data_product_attribute = models.CharField(max_length=200, blank=True, null=True)
    name_variants = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    ref_number = models.CharField(max_length=200, blank=True, null=True)
    
    link = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=10, default="New")

