from django.urls import path
from .views import *

urlpatterns = [
    path('s1/', SongInfo.as_view()),
    path('s1/<pk>/', SongDetails.as_view())

]