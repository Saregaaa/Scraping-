import sys
import os
import django

sys.path.append('D:\\work\\site\\vivarealcombr_project') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'vivarealcombr_project.settings'
django.setup()