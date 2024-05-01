from django.urls import path
from . views import BloodViews, DonerDetails, SearchDonorView, SearchBarDonorView
from . import views

urlpatterns = [
    path('Blood/<str:group>', views.BloodViews.as_view(), name='bloodbank'),
    path('Doner/Details/<int:pk>', views.DonerDetails.as_view(), name='donerdetails'),
    path('search/Donors/',views.SearchDonorView.as_view(), name="searchdonors"),
    path('searches/Donors/', views.SearchBarDonorView.as_view(), name="searchbar"),
    # path('Email/Donors/', views.send_Email_donor.as_view(), name="sendemail"),
]
