from django.urls import path
from .views import *

urlpatterns = [
    path('register', register),  # 指定register函数的路由为register
    path('login', login),
    path('uploadbook',savebook),
    path('uploadmovie',savemovie),
    path('uploadtele',savetele),
    path('movie/hot',hotmovie),
    path('tele/hot',hottele),
]
