from . import views
from django.urls import path

urlpatterns = [
    path('count-anomalies/', views.CountAnomalies.as_view(), name='count_anomalies'),
    path('count-anomalies/<str:sensor_id>/', views.CountAnomalies.as_view(), name='count_anomalies'),
    # path('count-anomalies/', views.count_anomalies(), name='count_anomalies'),
    # path('count-anomalies/', views.count_anomalies(), name='count_anomalies'),
]

# from rest_framework.routers import SimpleRouter, DefaultRouter
# router = DefaultRouter()
# router.register('count-anomalies', views.CountAnomalies.as_view(), basename='count_anomalies')
# urlpatterns = router.urls