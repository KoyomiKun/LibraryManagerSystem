# Generated by Django 3.0.5 on 2020-04-06 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20200406_1800'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='borrow',
            unique_together={('bno', 'cno')},
        ),
    ]
