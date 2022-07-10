from . import views
from django.urls import path

urlpatterns = [
    path('', views.CountAnomalies.as_view(), name='count_anomalies_landing'),
    path('count-anomalies/', views.CountAnomalies.as_view(), name='count_anomalies_landing'),
    path('count-anomalies/<str:sensor_id>/', views.CountAnomalies.as_view(), name='count_anomalies'),
]
