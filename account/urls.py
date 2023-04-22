from django.urls import path
from account.views import *
urlpatterns=[
    path('',Mhome.as_view()),
    path('regauth/',RegAuth.as_view(),name="regauth"),
    path('logauth/',LogAuth.as_view(),name="logauth"),
    path('logout/',LogAuth.as_view(),name="logout"),

]