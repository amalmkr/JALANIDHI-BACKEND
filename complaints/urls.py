from .views import ComplaintDetailsView,ComplaintListCreateView,ComplaintStatusView
from django.urls import path


urlpatterns=[
    path('complaint/',view=ComplaintListCreateView.as_view(),name="complain-list-created"),
    path('complaint/<int:id>/',view=ComplaintDetailsView.as_view(),name="Complaint-details"),
    path('complaint/<int:id>/status',view=ComplaintStatusView.as_view(),name="complaint-status")
]