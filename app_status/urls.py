from django.urls import path, include

from .views import *


urlpatterns = [
    path('stat_list', StatList.as_view(), name='stat_list'),
    path('stat_upda/<int:pk>', StatUpda.as_view(), name='stat_upda'),
    
    path('docs_crea', DocsCrea.as_view(), name='docs_crea'),
    path('docs_upda/<int:pk>', DocsUpda.as_view(), name='docs_upda'),
    path('docs_remo/<int:pk>', DocsRemo.as_view(), name='docs_remo'),
    
    path('qual_crea', QualCrea.as_view(), name='qual_crea'),
    path('qual_upda/<int:pk>', QualUpda.as_view(), name='qual_upda'),
    path('qual_remo/<int:pk>', QualRemo.as_view(), name='qual_remo'),
]

