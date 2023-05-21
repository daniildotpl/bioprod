from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm
from django.db.models.fields import EmailField
from django.forms import ClearableFileInput, ModelForm, TextInput, Textarea, PasswordInput, EmailInput, widgets
from django.contrib.auth.models import User
from django.http import request

from .models import *
from app_site.forms import *

from ckeditor.widgets import CKEditorWidget


class DocumentsForm(ModelForm):
    phot = forms.ImageField(label='Изображение',       widget=MyInputFile(attrs={'class': 'fil'}),                  required=True)
    titl = forms.CharField(label='Название документа', widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=True)
    seri = forms.CharField(label='Серия',              widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=False)
    numb = forms.CharField(label='Номер',              widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=False)

    class Meta:
        model = Documents
        fields = ('phot', 'titl', 'seri', 'numb')

class QualificationsForm(ModelForm):
    phot = forms.ImageField(label='Изображение',       widget=MyInputFile(attrs={'class': 'fil'}),                  required=True)
    titl = forms.CharField(label='Название заведения', widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=True)
    seri = forms.CharField(label='Серия',              widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=False)
    numb = forms.CharField(label='Номер',              widget=TextInput(attrs={'class': 'inp', 'placeholder': ''}), required=False)

    class Meta:
        model = Qualifications
        fields = ('phot', 'titl', 'seri', 'numb')

class StatusForm(ModelForm):
    CH = (('0', 'Без доступа'), ('1', 'Level I'), ('2', 'Level II'), ('3', 'Level III'),)
    stat = forms.ChoiceField(choices=CH, widget = forms.RadioSelect(), required=True)
    
    class Meta:
        model = Status
        fields = ('stat',)
