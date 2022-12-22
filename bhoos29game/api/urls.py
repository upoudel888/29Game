from . import views
from django.urls import path

urlpatterns = [
    path("",views.home, name='home'),
    path("hi/", views.hi, name = 'hi'),
    path("bid",views.bid, name='bid'),
    path("bid/",views.bid, name='bid1'),
    path('chooseTrump',views.chooseTrump,name='chooseTrump'),
    path('chooseTrump/',views.chooseTrump,name='chooseTrump1'),
    path('play',views.play,name='play'),
    path('play/',views.play,name='play/'),
]
