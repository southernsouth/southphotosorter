from django.contrib import admin
from .models import SystemSettings


class SystemSettingsAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in SystemSettings._meta.fields]

admin.site.register(SystemSettings, SystemSettingsAdmin)

admin.AdminSite.site_header = 'South Photo sorter'
admin.AdminSite.site_title = 'South Photo sorter'
admin.site.index_title = 'South Photo sorter'
