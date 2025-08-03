import sys
import os
import django

sys.path.append('D:\\work\\site\\foursquarecom_project') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'foursquarecom_project.settings'
django.setup()