from django.urls import path
from . views import Home, Registration, LoginViews, LogoutView, ProfileViews
from . import views

urlpatterns = [
    path('',Home.as_view(), name="home"),
    path('register/', Registration.as_view(), name="register"),
    path('login/', LoginViews.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileViews.as_view(), name='profile')
]
