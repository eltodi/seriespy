'''
import sys
import site
import os


#VIRTUALENV = '/var/virtualenvs/ponysite.example.com/lib/python2.4/site-packages'
VIRTUALENV = '/home/eliast/.virtualenvs/pony.example.com/lib/python2.7/site-packages'

WEBAPPS_PATH = '/var/webapps'
 

prev_sys_path = list(sys.path)

# add the site-packages of our virtualenv as a site dir
site.addsitedir(VIRTUALENV)

# add the app's directory to the PYTHONPATH
sys.path.append(WEBAPPS_PATH)

# reorder sys.path so new directories from the addsitedir show up first
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

# import from down here to pull in possible virtualenv django install
os.environ['DJANGO_SETTINGS_MODULE'] = 'pony.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
'''

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'pony.settings'

#path = '/furanet/sites/innovalocal.org/web/htdocs'
path = '/var/webapps/pony/'


if path not in sys.path:
    sys.path.append(path)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

