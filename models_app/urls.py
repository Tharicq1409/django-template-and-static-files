from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="indexpage"),
    path('base',views.base,name="basepages"),
    path('blogpost/',views.blog,name="blogpage"),
]