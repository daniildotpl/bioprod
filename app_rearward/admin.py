from django.contrib import admin

from app_rearward.models import *



class MedicinesInLIne(admin.TabularInline):
    model = Medicines
    extra = 1


# Перерегистрируем модель Faks
class FaksAdmin(admin.ModelAdmin):
    list_display = ['titl']
    inlines = [MedicinesInLIne]
admin.site.register(Faks, FaksAdmin)


# Перерегистрируем модель Medicines
class MedicinesAdmin(admin.ModelAdmin):
    list_display = ['titl']
admin.site.register(Medicines, MedicinesAdmin)


# Перерегистрируем модель Locations
class LocationsAdmin(admin.ModelAdmin):
    list_display = ['titl']
admin.site.register(Locations, LocationsAdmin)