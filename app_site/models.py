from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField



class User(AbstractUser):
    email     = models.EmailField(unique=True)
    patr_name = models.CharField(max_length=255,                    verbose_name="Отчество",           null=True, blank=True)
    toke      = models.CharField(max_length=255,                    verbose_name="Токен для проверки", null=True, blank=True)
    phon      = models.CharField(max_length=15,                     verbose_name="Телефон",            null=True, blank=True)
    phot      = models.ImageField(upload_to="photos/%Y/%m/%d",      verbose_name="Фото пользователя",  null=True, blank=True)
    auth      = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name="Author",             null=True, blank=True, related_name = 'auth_user')
    dele      = models.BooleanField(default=False,                  verbose_name="Deleted",            null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = User.objects.get(pk=self.pk)
            if old_self.phot and self.phot != old_self.phot:
                old_self.phot.delete(False)
        return super().save(*args, **kwargs)
    

class Info(models.Model):
    titl = models.CharField(max_length=255,                    verbose_name="Title")
    desc = models.TextField(                                   verbose_name="Description",        null=True, blank=True)
    cont = RichTextField(                                      verbose_name="Content",            null=True, blank=True)
    phot = models.ImageField(upload_to="photos/%Y/%m/%d",      verbose_name="Фото пользователя",  null=True, blank=True)
    auth = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name="Author",             null=True, blank=True, related_name = 'info')
    dele = models.BooleanField(default=False,                  verbose_name="Deleted",            null=True, blank=True)
    publ = models.BooleanField(default=False,                  verbose_name="Published",          null=True, blank=True)

    def __str__(self):
        return self.titl

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = Info.objects.get(pk=self.pk)
            if old_self.phot and self.phot != old_self.phot:
                old_self.phot.delete(False)
        return super().save(*args, **kwargs)


class PersMenu(models.Model):
    titl = models.CharField(max_length=255,                    verbose_name="Title")
    urll = models.CharField(max_length=255,                    verbose_name="URL")
    phot = models.ImageField(upload_to="photos/%Y/%m/%d",      verbose_name="Фото пользователя",                 null=True, blank=True)
    publ = models.BooleanField(default=False,                  verbose_name="Published")
    grou = models.ManyToManyField(Group,                       verbose_name="Groups", related_name = 'persmenu')

    def __str__(self):
        return self.titl

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = PersMenu.objects.get(pk=self.pk)
            if old_self.phot and self.phot != old_self.phot:
                old_self.phot.delete(False)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Меню кабинета'
        verbose_name_plural = 'Меню кабинета'
        ordering = ['pk',]