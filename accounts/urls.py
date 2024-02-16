from django.urls import path
from . views import Home, Registration, LoginViews, LogoutView, ProfileViews, ProfileUpdateView, HistoryView, StatusChangeView,  HistoryUpdateView
from . import views
from . views import AddHistoryView

urlpatterns = [
    path('',Home.as_view(), name="home"),
    path('register/', Registration.as_view(), name="register"),
    path('login/', LoginViews.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileViews.as_view(), name='profile'),
    path('profile/update/<int:pk>', ProfileUpdateView.as_view(), name='updateprofile'),
    path('Donor/history/<int:pk>/',HistoryView.as_view(), name="history"),
    path('Donor/history/add/<int:pk>/',AddHistoryView.as_view(), name="addhistory"),
    path('Donor/Change/Status/<int:pk>/',StatusChangeView.as_view(), name="statuschange"), 
    path('history/update/<int:pk><int:pk1>', HistoryUpdateView.as_view(), name="historyupdate" ),
]
