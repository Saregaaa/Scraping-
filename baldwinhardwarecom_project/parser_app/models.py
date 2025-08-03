from django.db import models

# Create your models here.
class Product(models.Model):

    title = models.CharField(max_length=255, blank=True, null=True) 
    model_number = models.CharField(max_length=255, blank=True, null=True)
    image_list = models.JSONField(blank=True, null=True)
    key_features_list = models.JSONField(blank=True, null=True)
    features_list = models.JSONField(blank=True, null=True)
    specifications_list = models.JSONField(blank=True, null=True)
    documents_list = models.JSONField(blank=True, null=True)

    product_link = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=10, default='New')

    def __str__(self):
        return self.title