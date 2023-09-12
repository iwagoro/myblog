from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),  #views.post_listをルートURLに割り当てる
]