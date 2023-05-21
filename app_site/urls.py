from django.urls import path, include

from .views import *


urlpatterns = [

    path('', Pers.as_view(), name='site'),
    path('somewrong', Somewrong.as_view(), name='somewrong'),
    path('sear_resu', SearResu.as_view(), name='sear_resu'),
    path('test', Test.as_view(), name='test'),

    path('lgn', Lgn.as_view(), name='lgn'),
    path('lgt', Lgt.as_view(), name='lgt'),

    path('regi', Regi.as_view(), name='regi'),
    path('regi_done', RegiDone.as_view(), name='regi_done'),
    path('regi_conf/<token>', RegiConf.as_view(), name='regi_conf'),

    path('rese', Rese.as_view(), name='rese'),                                     # PasswordResetView
    path('rese_done/', ReseDone.as_view(), name='rese_done'),                      # PasswordResetDoneView
    path('rese_conf/<uidb64>/<token>/', ReseConf.as_view(), name='rese_conf'),     # PasswordResetConfirmView
    path('rese_cmpl/', ReseCmpl.as_view(), name='rese_cmpl'),                      # PasswordResetCompleteView

    path('pers', Pers.as_view(), name='pers'),
    path('pers_upda/<user_id>', PersUpda.as_view(), name='pers_upda'),
    path('pers_remo/<user_id>', PersRemo.as_view(), name='pers_remo'),

]

