from django.urls import path
from . views import BloodViews, DonerDetails
from . import views

urlpatterns = [
    path('Blood/<str:group>', views.BloodViews.as_view(), name='bloodbank'),
    path('Doner/Details/<int:pk>', views.DonerDetails.as_view(), name='donerdetails'),
]
