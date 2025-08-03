import sys
import os
import django

sys.path.append('D:\\work\\site\\goldpetpt_project') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'goldpetpt_project.settings'
django.setup()