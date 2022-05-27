from django.urls import path
from .views import *

urlpatterns = [
    path('detail', detail),
    path('article/hot', hot_article),
    path('article/new', new_article),
]
