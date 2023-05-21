from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .models import *
from .forms import *



# Перерегистрируем модель User
class UserAdmin(admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    change_password_form = AdminPasswordChangeForm
    list_display = ['username', 'email', 'is_superuser', 'is_staff', 'is_active']

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults.update({
                'form': self.add_form,
            })
        defaults.update(kwargs)
        return super(UserAdmin, self).get_form(request, obj, **defaults)

admin.site.register(User, UserAdmin)


# Перерегистрируем модель PersMenu
class PersMenuAdmin(admin.ModelAdmin):
    list_display = ['titl', 'publ']

admin.site.register(PersMenu, PersMenuAdmin)
