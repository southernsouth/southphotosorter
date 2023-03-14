import os, sys

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from django.core.management.base import BaseCommand
from django.db.models import Sum, Q, F, Max

from photosorter.models import SystemSettings


def get_key():
    return list(SystemSettings.objects.values_list('key'))[0][0]
