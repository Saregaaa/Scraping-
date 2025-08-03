from django.db import models

# Create your models here.
class Ads(models.Model):

    page_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    caption = models.CharField(max_length=500, blank=True, null=True)
    link_description = models.TextField(blank=True, null=True)
    link_url = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    page_categories = models.CharField(max_length=500, blank=True, null=True)
    video_sd_url = models.TextField(blank=True, null=True)
    start_date = models.CharField(max_length=100, blank=True, null=True)
    collation_id = models.CharField(max_length=100, blank=True, null=True)
    page_id = models.CharField(max_length=100, blank=True, null=True)
    
    ad_archive_id = models.CharField(max_length=100, unique=True)