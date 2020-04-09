# Generated by Django 3.0.5 on 2020-04-03 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bno', models.CharField(editable=False, max_length=8, primary_key=True, serialize=False, verbose_name='book_number')),
                ('category', models.CharField(editable=False, max_length=10, verbose_name='category')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('press', models.CharField(max_length=30, verbose_name='press')),
                ('year', models.PositiveIntegerField(verbose_name='year')),
                ('author', models.CharField(max_length=20, verbose_name='author')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='price')),
                ('total', models.PositiveIntegerField(verbose_name='total')),
                ('stock', models.PositiveIntegerField(verbose_name='stock')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Book',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('cno', models.CharField(editable=False, max_length=7, primary_key=True, serialize=False, verbose_name='card_number')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
                ('department', models.CharField(max_length=40, verbose_name='department')),
                ('type', models.CharField(choices=[('T', 'teacher'), ('G', 'graduate'), ('U', 'user'), ('O', 'operator')], max_length=1, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Card',
            },
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(verbose_name='borrow_date')),
                ('return_date', models.DateTimeField(null=True, verbose_name='return_date')),
                ('bno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book', verbose_name='card_number')),
                ('cno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Card', verbose_name='book_number')),
            ],
            options={
                'verbose_name': 'Borrow',
                'verbose_name_plural': 'Borrow',
            },
        ),
    ]