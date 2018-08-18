import os  

from django.contrib.auth.hashers import make_password, check_password


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.mysite.settings'  
print(make_password("1", None, 'pbkdf2_sha256'))

