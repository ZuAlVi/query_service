from datetime import datetime
import requests


from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from query_service.models import Query
from query_service.serializers import QuerySerializer


class QueryView(APIView):
    """
    - Принимает данные запроса (кадастровый номер, широту, долготу)
    - Создает экземпляр модели Query с данными запроса
    - Эмулирует отправку запроса на внешний сервер (задержка до 60 секунд)
    - Генерирует случайный ответ (true или false)
    - Сохраняет ответ и время получения ответа в модели Query
    - Возвращает ответ
    """
    def post(self, request):
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.save()
            external_service_url = "http://127.0.0.1:5000/external_service"
            response = requests.post(external_service_url)
            response_data = response.json()
            query.response = response_data['response']
            query.response_time = datetime.now()
            query.save()
            return Response({"response": response}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultView(APIView):
    """
    - Принимает ответ от внешнего сервиса
    - Обновляет соответствующий экземпляр модели Query с ответом и временем получения ответа
    """
    def post(self, request):
        query_id = request.data.get('query_id')
        response = request.data.get('response')
        query = get_object_or_404(Query, id=query_id)
        query.response = response
        query.response_time = datetime.now()
        query.save()
        return Response({"massage": "Result updated successfully"}, status=status.HTTP_200_OK)


class HistoryView(APIView):
    """
    - Возвращает список всех экземпляров модели Query (историю запросов)
    """
    def get(self, request):
        queries = Query.objects.all()
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)


class HistoryByNumberView(APIView):
    """
    - Принимает кадастровый номер в URL
    - Возвращает список экземпляров модели Query с указанным кадастровым номером
    """
    def get(self, request, cadastral_number):
        queries = Query.objects.filter(cadastral_number=cadastral_number)
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)


class PingView(APIView):
    """
    - Представление для проверки работоспособности сервера (возвращает "pong")
    """
    def get(self, request):
        return Response({"message": "pong"})
