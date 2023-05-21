from django.db import models
from django.utils.translation import gettext_lazy as _

from app_site.models import User



class Documents(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь",   related_name = 'passport')
    phot = models.ImageField(upload_to="photos/%Y/%m/%d",    verbose_name="Документ",       null=True, blank=True)
    titl = models.CharField(max_length=255,                  verbose_name="Документ",       null=True, blank=True)
    seri = models.CharField(max_length=15,                   verbose_name="Серия паспорта", null=True, blank=True)
    numb = models.CharField(max_length=15,                   verbose_name="Номер паспорта", null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = Documents.objects.get(pk=self.pk)
            if old_self.phot and self.phot != old_self.phot:
                old_self.phot.delete(False)
        return super().save(*args, **kwargs)

class Qualifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь",    related_name = 'diploma')
    phot = models.ImageField(upload_to="photos/%Y/%m/%d",      verbose_name="Диплом",        null=True, blank=True)
    titl = models.CharField(max_length=255,                    verbose_name="ВУЗ",           null=True, blank=True)
    seri = models.CharField(max_length=15,                     verbose_name="Номер диплома", null=True, blank=True)
    numb = models.CharField(max_length=15,                     verbose_name="Номер диплома", null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_self = Qualifications.objects.get(pk=self.pk)
            if old_self.phot and self.phot != old_self.phot:
                old_self.phot.delete(False)
        return super().save(*args, **kwargs)

class Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Пользователь",    related_name = 'status')
    stat = models.CharField(max_length=225,                     verbose_name="Уровень доступа", null=True, blank=True)
    hash = models.CharField(max_length=225,                     verbose_name="Хэш код",         null=True, blank=True)
    # qrco = models.ImageField(upload_to="photos/%Y/%m/%d",    verbose_name="QR код",       null=True, blank=True)
    
    def __str__(self):
        return str(self.user)
