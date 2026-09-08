from django.urls import path
from .views import BillListCreateView,Billdetails,Paymentdetails,PaymentListCreateView


urlpatterns=[
    path("bills/",BillListCreateView.as_view(),name="bill-list-create"),
    path("bills/<int:id>/",Billdetails.as_view(),name="bill-details"),
    path("payments/",PaymentListCreateView.as_view(),name="payment-list-create"),
    path("payments/<int:id>/",Paymentdetails.as_view(),name="payment-details")
]