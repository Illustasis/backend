from django.urls import path
from .views import *

urlpatterns = [
    path('detail', detail),
    path('collect',collect),
    path('uncollect',uncollect),
    path('hot', hot),
    path('high', high),
    path('collection', collection),
    path('star',star),
    path('passage', passage),
    path('mypassage', my_article),
]