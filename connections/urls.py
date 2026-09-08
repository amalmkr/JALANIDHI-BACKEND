from django.urls import path
from .views import ConnectionsListCreateView,ConnectionDetailView

urlpatterns=[
    path("connections/",ConnectionsListCreateView.as_view(),name="connection-list-created"),
    path("connections/<int:id>/",ConnectionDetailView.as_view(),name="Connection-details")
]