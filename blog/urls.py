from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),  #views.post_listをルートURLに割り当てる
    path('post/<int:pk>/',views.post_detail,name='post_detail')
]