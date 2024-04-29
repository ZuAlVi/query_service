from django.urls import path, include, re_path
from query_service import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('query/', views.QueryView.as_view(), name='query'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('history/', views.HistoryView.as_view(), name='history'),
    path('history/<str:cadastral_number>/', views.HistoryByNumberView.as_view(), name='history_by_number'),
    path('ping/', views.PingView.as_view(), name='ping'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
