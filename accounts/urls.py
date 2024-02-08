from django.urls import path
from . views import Home, Registration, LoginViews
from . import views

urlpatterns = [
    path('',Home.as_view(), name="home"),
    path('register/', Registration.as_view(), name="register"),
    path('login/', LoginViews.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
]
