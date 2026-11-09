from django.urls import path
from .views import *

urlpatterns = [
    path('games/', GameList.as_view(), name='games')
]
