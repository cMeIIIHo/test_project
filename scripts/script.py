import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')

import django
django.setup()

from ad.models import *

print(Channel.objects.all())