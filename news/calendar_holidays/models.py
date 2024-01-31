from django.db import models

class Holidays(models.Model):
    holiday = models.DateField(verbose_name='Дата выходного/праздника')

    def __str__(self):
        return f'Выходной или праздник - {self.holiday}'

    class Meta:
        verbose_name='Каледндарь выходных'
        verbose_name_plural='Календари выходных'

