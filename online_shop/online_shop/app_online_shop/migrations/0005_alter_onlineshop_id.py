# Generated by Django 4.2.1 on 2023-08-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_online_shop', '0004_alter_onlineshop_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlineshop',
            name='id',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]