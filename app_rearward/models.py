from django.db import models

from app_site.models import User


class Locations(models.Model):
    titl = models.CharField(verbose_name="Локация", max_length=225)
    coor = models.CharField(verbose_name="Координаты", max_length=225)
    
    def __str__(self):
        return str(self.titl)
    
    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        # ordering = ['-time_crea',]


class Faks(models.Model):
    titl = models.CharField(verbose_name="Аптечка", max_length=225)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Средства", related_name = 'user')
    
    def __str__(self):
        return str(self.titl)
    
    class Meta:
        verbose_name = 'Аптечка'
        verbose_name_plural = 'Аптечки'
        # ordering = ['-time_crea',]


class Medicines(models.Model):
    titl = models.CharField(max_length=225,                  verbose_name="Препарат")
    befo = models.CharField(max_length=225,                  verbose_name="Годен до", null=True, blank=True)
    faks = models.ForeignKey(Faks, on_delete=models.PROTECT, verbose_name="Средства", related_name = 'medicines', null=True, blank=True)
    
    def __str__(self):
        return str(self.titl)
    
    class Meta:
        verbose_name = 'Средство'
        verbose_name_plural = 'Средства'
        # ordering = ['-time_crea',]
