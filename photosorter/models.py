from django.db import models


class SystemSettings(models.Model):
    key = models.CharField('Key', max_length = 500)
