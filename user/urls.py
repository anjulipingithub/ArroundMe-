from django.urls import path
from user.views import *

urlpatterns = [
    path('home/',uhome.as_view(),name="uh"),
    path('pro/',profile.as_view(),name="pro"),
    path('bio/',BioView.as_view(),name="bio"),
    path('editbio/<int:pk>',EditbioView.as_view(),name="ebio"),
    path('editpass/',EditPassword.as_view(),name="cpswd"),
    path('mpost/',MyPosts.as_view(),name="mpost"),
    path('epost//<int:pk>',EditpostView.as_view(),name="epost"),
    path('dpost//<int:pk>',DeletepostView.as_view(),name="dpost"),
    path('addcmnt/<int:pid>',addcomment,name="addc"),
    path('addlike/<int:pid>',addlike,name="addl"),
]