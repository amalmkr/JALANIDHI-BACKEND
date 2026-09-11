from django.urls import path
from .views import ConnectionsListCreateView,ConnectionDetailView,ConnectionApproveView

urlpatterns=[
    path("connections/",ConnectionsListCreateView.as_view(),name="connection-list-created"),
    path("connections/<int:id>/",ConnectionDetailView.as_view(),name="Connection-details"),
    path("connections/<int:id>/approve/",ConnectionApproveView.as_view(),name="connection-approve"),
]

