from django.contrib import admin
from query_service.models import Query


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'cadastral_number',
                    'latitude', 'longitude',
                    'request_time',
                    'response_time',
                    'response')
