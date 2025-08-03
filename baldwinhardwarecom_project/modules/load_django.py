import sys
import os
import django

sys.path.append('D:\\work\\site\\baldwinhardwarecom_project') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'baldwinhardwarecom_project.settings'
django.setup()