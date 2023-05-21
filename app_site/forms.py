from functools import partial
from django import forms
from django.forms import TextInput, PasswordInput, EmailInput, HiddenInput
from django.forms.widgets import CheckboxInput, ClearableFileInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

from .models import User


DateInput = partial(forms.DateInput)


# --- MyWidgets -------------------------------------
class MyInputCheckbox(CheckboxInput):
    template_name = 'django/forms/widgets/my_input_checkbox.html'

    def get_context(self, name, value, attrs, **kwargs):
        context = super().get_context(name, value, attrs, **kwargs)
        return context

class MyInputFile(ClearableFileInput):
    template_name = 'django/forms/widgets/my_input_file.html'

class MyInputFileMultiple(ClearableFileInput):
    template_name = 'django/forms/widgets/my_input_file_multiple.html'


# --- Gete -------------------------------------------
class LgnForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'inp',     'placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'inp', 'placeholder': 'Password'}))

class RgtForm(UserCreationForm):
    username =  forms.CharField(   widget=TextInput(attrs={'class': 'inp',     'placeholder': 'Login'}))
    email =     forms.EmailField(  widget=EmailInput(attrs={'class': 'inp',    'placeholder': 'Email'}))
    password1 = forms.CharField(   widget=PasswordInput(attrs={'class': 'inp', 'placeholder': 'Password'}))
    password2 = forms.CharField(   widget=PasswordInput(attrs={'class': 'inp', 'placeholder': 'Password else'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# --- Reset Password --------------------------------
class ReseForm(PasswordResetForm):
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'inp', 'placeholder': 'Email'}))

class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(   widget=PasswordInput(attrs={'class': 'inp', 'placeholder': 'Password'}))
    new_password2 = forms.CharField(   widget=PasswordInput(attrs={'class': 'inp', 'placeholder': 'Password else'}))


# --- Change Password -------------------------------
class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль",   widget=forms.PasswordInput(attrs={'class': 'inp', 'placeholder': 'Старый пароль'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'inp', 'placeholder': 'Новый пароль'}))
    new_password2 = forms.CharField(label="Новый пароль (повторно)", widget=forms.PasswordInput(attrs={'class': 'inp', 'placeholder': 'Новый пароль (повторно)'}))


# --- Facking Shit for Admin panel ------------------
class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_active', 'last_name', 'first_name', 'patr_name', 'phot', 'groups', 'phon', 'password')

class AdminPasswordChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('password',)


# --- Searching -------------------------------------
class SearForm(forms.Form):
    quer = forms.CharField(widget=TextInput(attrs={'placeholder': 'Поиск'}))


# --- Update User ----------------------------------
class UserFormUpda(forms.ModelForm):
    username   = forms.CharField(label='Login',          widget=TextInput(attrs={ 'class': 'inp', 'placeholder': 'Login'}))
    email      = forms.EmailField(label='Email',         widget=EmailInput(attrs={'class': 'inp', 'placeholder': 'Email'}))
    last_name  = forms.CharField(label='Фамилия',        widget=TextInput(attrs={ 'class': 'inp', 'placeholder': 'Фамилия'}),             required=False)
    first_name = forms.CharField(label='Имя',            widget=TextInput(attrs={ 'class': 'inp', 'placeholder': 'Имя'}),                 required=False)
    patr_name  = forms.CharField(label='Отчество',       widget=TextInput(attrs={ 'class': 'inp', 'placeholder': 'Отчество'}),            required=False)
    phon       = forms.CharField(label='Телефон',        widget=TextInput(attrs={ 'class': 'inp', 'placeholder': 'Телефон'}),             required=False)
    phot       = forms.ImageField(label='Photo',         widget=MyInputFile(attrs={'class': 'fil'}),                            required=False)
    
    class Meta:
        model = User
        fields = [ 'username', 'email', 'last_name', 'first_name', 'patr_name', 'phon', 'phot' ]

