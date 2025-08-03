from django.db import models


class LinkAds(models.Model):
    link_ads = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=10, default='New')

    def __str__(self):
        return self.link_ads
    

class LinkAgent(models.Model):
    link = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=10, default='New')

    def __str__(self):
        return self.link
    

class Agent(models.Model):
    account_name = models.CharField(max_length=500, null=True, blank=True) 
    account_id = models.CharField(max_length=500, null=True, blank=True)
    license_number = models.CharField(max_length=500, null=True, blank=True)
    phone_primary = models.CharField(max_length=500, null=True, blank=True)
    phone_mobile = models.CharField(max_length=500, null=True, blank=True)
    website_url = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)
    zip_code = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    street_number = models.CharField(max_length=500, null=True, blank=True)
    street = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    neighborhood = models.CharField(max_length=500, null=True, blank=True)
    logo_url = models.CharField(max_length=500, null=True, blank=True)

    link = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=10, default='New')

    def __str__(self):
        return self.account_name
    
