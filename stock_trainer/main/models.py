from django.db import models


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField('Название актива', max_length=100)
    num = models.IntegerField('Кол-во')
    price = models.IntegerField('Цена')
    month = models.IntegerField('Месяц')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Актив'
        verbose_name_plural = 'Активы'

