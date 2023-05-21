from django.contrib import admin
from .models import *


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'stat']

admin.site.register(Status, StatusAdmin)


