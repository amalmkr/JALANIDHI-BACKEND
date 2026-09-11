
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("users.urls")),
    path('api/',include("connections.urls")),
    path('api/',include("meter_readings.urls")),
    path('api/',include("complaints.urls")),
    path('api/',include("billing.urls")),

    path(
    "media/<path:path>",
    serve,
    {"document_root":settings.MEDIA_ROOT},
),
]

