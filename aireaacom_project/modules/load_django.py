import sys
import os
import django

sys.path.append('D:\\work\\site\\aireaacom_project') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'aireaacom_project.settings'
django.setup()