import sys
import os
import django

sys.path.append('D:\\work\\site\\bahtsoldcom_project') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'bahtsoldcom_project.settings'
django.setup()