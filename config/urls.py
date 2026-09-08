
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("users.urls")),
    path('api/',include("connections.urls")),
    path('api/',include("meter_readings.urls")),
    path('api/',include("complaints.urls")),
    path('api/',include("billing.urls")),
]
