from django.urls import path
from .views import *

urlpatterns = [
    path('bookcomment', bookcomment),
    path('dt',dt)
]
