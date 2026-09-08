from django.urls import path
from .views import MeterReadingListCreateView, MeterReadingDetails

urlpatterns = [
    path("meter_readings/",MeterReadingListCreateView.as_view(),name="meter-reading-list-create"),
    path("meter_readings/<int:id>/",MeterReadingDetails.as_view(),name="meter-reading-detail"),
]