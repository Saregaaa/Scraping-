from django.db import models

# Create your models here.

class Link(models.Model):
    
    link = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=10, default='New')

    def __str__(self):
        return self.link
    

class Customer(models.Model):
    
    name = models.CharField(max_length=255, blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    website_link = models.CharField(max_length=255, blank=True, null=True)
    calendar = models.CharField(max_length=255, blank=True, null=True)

    profile_link = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class CustomerDub(models.Model):
    
    name = models.CharField(max_length=255, blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    website_link = models.CharField(max_length=255, blank=True, null=True)
    calendar = models.CharField(max_length=255, blank=True, null=True)

    profile_link = models.CharField(max_length=255, blank=True, null=True)
    link_sale = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name