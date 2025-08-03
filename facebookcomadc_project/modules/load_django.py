import sys
import os
import django

sys.path.append('D:\\work\\site\\facebookcomadc_project') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'facebookcomadc_project.settings'
django.setup()