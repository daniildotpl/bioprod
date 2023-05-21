from django.urls import path, include

from .views import *


urlpatterns = [
    path('loca_crea', LocaCrea.as_view(), name='loca_crea'),
    path('loca_list', LocaList.as_view(), name='loca_list'),
    path('loca_upda/<int:pk>', LocaUpda.as_view(), name='loca_upda'),
    path('loca_remo/<int:pk>', LocaRemo.as_view(), name='loca_remo'),
    
    path('faks_list', FaksList.as_view(), name='faks_list'),
    path('faks_crea', FaksCrea.as_view(), name='faks_crea'),
    path('faks_upda/<int:pk>', FaksUpda.as_view(), name='faks_upda'),
    # path('faks_upda_medi/<int:pk>', FaksUpdaMedi.as_view(), name='faks_upda_medi'),
    path('faks_remo/<int:pk>', FaksRemo.as_view(), name='faks_remo'),
    
    path('medi_list', MediList.as_view(), name='medi_list'),
    path('medi_crea', MediCrea.as_view(), name='medi_crea'),
    path('medi_upda/<int:pk>', MediUpda.as_view(), name='medi_upda'),
    path('medi_remo/<int:pk>', MediRemo.as_view(), name='medi_remo'),
]

