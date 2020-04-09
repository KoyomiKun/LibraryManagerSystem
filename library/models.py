from django.db import models


# Create your models here.

class Book(models.Model):
    bno = models.CharField(max_length=8, verbose_name='book_number', editable=False, primary_key=True)
    catagory = models.CharField(max_length=10, verbose_name='catagory', editable=False)
    title = models.CharField(max_length=40, verbose_name='title')
    press = models.CharField(max_length=30, verbose_name='press')
    year = models.PositiveIntegerField(verbose_name='year')
    author = models.CharField(max_length=20, verbose_name='author')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='price')
    total = models.PositiveIntegerField(verbose_name='total')
    stock = models.PositiveIntegerField(verbose_name='stock')

    class Meta:
        verbose_name = verbose_name_plural = 'Book'


class Card(models.Model):
    TYPE_ITEMS = (
        ('T', 'teacher'),
        ('G', 'graduate'),
        ('U', 'user'),
        ('O', 'operator')
    )
    cno = models.CharField(max_length=7, verbose_name='card_number', editable=False, primary_key=True)
    name = models.CharField(max_length=10, verbose_name='name')
    department = models.CharField(max_length=40, verbose_name='department')
    type = models.CharField(max_length=1, verbose_name='name', choices=TYPE_ITEMS)

    class Meta:
        verbose_name = verbose_name_plural = 'Card'


class Borrow(models.Model):
    bno = models.ForeignKey('Book', on_delete=models.CASCADE, verbose_name='card_number')
    cno = models.ForeignKey('Card', on_delete=models.CASCADE, verbose_name='book_number')
    borrow_date = models.DateTimeField(auto_now_add=False, verbose_name='borrow_date')
    return_date = models.DateTimeField(auto_now_add=False, verbose_name='return_date', null=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Borrow'
