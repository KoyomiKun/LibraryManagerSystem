# Generated by Django 3.0.5 on 2020-04-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20200408_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=40, verbose_name='category'),
        ),
    ]