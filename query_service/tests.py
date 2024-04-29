from query_service.models import Query
from query_service.serializers import QuerySerializer

from django.test import TestCase
from rest_framework.test import APITestCase

from django.urls import reverse
from rest_framework import status




class QueryModelTestCase(TestCase):
    def test_query_str_representation(self):
        query = Query.objects.create(
            cadastral_number='123456789',
            latitude=45.123,
            longitude=78.456
        )
        self.assertEqual(str(query), f'Query {query.id} (123456789)')


class QueryViewTestCase(APITestCase):
    def test_query_view(self):
        url = reverse('query')
        data = {
            'cadastral_number': '123456789',
            'latitude': 45.123,
            'longitude': 78.456
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Query.objects.filter(cadastral_number='123456789').exists())

    def test_history_view(self):
        url = reverse('history')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Query.objects.count())

    def test_history_by_number_view(self):
        query = Query.objects.create(
            cadastral_number='123456789',
            latitude=45.123,
            longitude=78.456
        )
        url = reverse('history_by_number', args=['123456789'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['cadastral_number'], '123456789')

    def test_ping_view(self):
        url = reverse('ping')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'pong'})


class QuerySerializerTestCase(TestCase):
    def test_query_serializer(self):
        query = Query.objects.create(
            cadastral_number='123456789',
            latitude=45.123,
            longitude=78.456
        )
        serializer = QuerySerializer(instance=query)
        expected_data = {
            'id': query.id,
            'cadastral_number': '123456789',
            'latitude': 45.123,
            'longitude': 78.456,
            'request_time': serializer.data['request_time'],
            'response_time': serializer.data['response_time'],
            'response': None
        }
        self.assertEqual(serializer.data, expected_data)
