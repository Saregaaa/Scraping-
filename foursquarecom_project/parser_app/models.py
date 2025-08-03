from django.db import models
from django.contrib.postgres.fields import ArrayField

class Company(models.Model):

     # User info
    user_id = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    private_profile = models.BooleanField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)  
    following_relationship = models.CharField(max_length=200, null=True, blank=True) 
    photo = models.CharField(max_length=255, null=True, blank=True)

    # General data
    name = models.CharField(max_length=200, null=True, blank=True)
    
    # Contact details
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    country_code = models.CharField(max_length=200, null=True, blank=True)
    
    # Data by category
    category_name = models.CharField(max_length=200, null=True, blank=True)
    category_code = models.CharField(max_length=200, null=True, blank=True)
    # category_icon = models.CharField(max_length=200, null=True, blank=True)
    
    # Rating data
    rating = models.CharField(max_length=200, null=True, blank=True)
    rating_signals = models.CharField(max_length=200, null=True, blank=True)
    user_count = models.CharField(max_length=200, null=True, blank=True)
    
    # Price data
    price_tier = models.CharField(max_length=200, null=True, blank=True)
    currency = models.CharField(max_length=200, null=True, blank=True)
    
    # Menu information
    menu_url = models.CharField(max_length=200, null=True, blank=True)
       
    # Metadata
    popularity_by_geo = models.CharField(max_length=200, null=True, blank=True)
    context_geo_id = models.CharField(max_length=200, null=True, blank=True)
    
    link = models.CharField(max_length=200, null=True, blank=True)

    venue_id = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=10, default="New")
    
    def __str__(self):
        return f"Name: {self.name}"
    
    class Meta:
        verbose_name = "Company"
    

class ZipCode(models.Model):
    zip_code = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=200, default="New")

    def __str__(self):
        return self.zip_code