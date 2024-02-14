from django.urls import path
from . views import Home, Registration, LoginViews, LogoutView, ProfileViews, ProfileUpdateView
from . import views

urlpatterns = [
    path('',Home.as_view(), name="home"),
    path('register/', Registration.as_view(), name="register"),
    path('login/', LoginViews.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileViews.as_view(), name='profile'),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view(), name='updateprofile'),
]
