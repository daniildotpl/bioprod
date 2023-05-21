from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm
from django.db.models.fields import EmailField
from django.forms import ClearableFileInput, ModelForm, TextInput, Textarea, PasswordInput, EmailInput, widgets
from django.contrib.auth.models import User
from django.http import request

from .models import *
from app_site.forms import *

from ckeditor.widgets import CKEditorWidget


class LocaForm(ModelForm):
    titl = forms.CharField(label='Локация',    widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=True)
    coor = forms.CharField(label='Координаты', widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=False)

    class Meta:
        model = Locations
        fields = ('titl',)


class FaksForm(ModelForm):
    titl = forms.CharField(label='Аптечка', widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=True)

    class Meta:
        model = Faks
        fields = ('titl',)


class MediForm(ModelForm):
    titl = forms.CharField(label='Медикомент', widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=True)
    befo = forms.CharField(label='Годен до', widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=True)

    class Meta:
        model = Medicines
        fields = ('titl', 'befo',)

