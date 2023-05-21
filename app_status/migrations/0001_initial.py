# Generated by Django 4.0.4 on 2023-05-21 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(blank=True, max_length=225, null=True, verbose_name='Уровень доступа')),
                ('hash', models.CharField(blank=True, max_length=225, null=True, verbose_name='Хэш код')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='status', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phot', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Диплом')),
                ('titl', models.CharField(blank=True, max_length=255, null=True, verbose_name='ВУЗ')),
                ('seri', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер диплома')),
                ('numb', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер диплома')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='diploma', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phot', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Документ')),
                ('titl', models.CharField(blank=True, max_length=255, null=True, verbose_name='Документ')),
                ('seri', models.CharField(blank=True, max_length=15, null=True, verbose_name='Серия паспорта')),
                ('numb', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер паспорта')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='passport', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
