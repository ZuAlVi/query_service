from django.db import models


class Query(models.Model):
    cadastral_number = models.CharField(max_length=100, verbose_name='Кадастровый номер')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    request_time = models.DateTimeField(auto_now_add=True, verbose_name='Время запроса')
    response_time = models.DateTimeField(auto_now_add=True, verbose_name='Время ответа')
    response = models.BooleanField(null=True, blank=True, verbose_name='Статус ответа')

    def __str__(self):
        return f'Query {self.id} ({self.cadastral_number})'

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
