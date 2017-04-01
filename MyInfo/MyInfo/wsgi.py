import os, sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.py'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
