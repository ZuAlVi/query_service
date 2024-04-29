from rest_framework import serializers
from query_service.models import Query


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'
