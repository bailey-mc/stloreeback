from django.urls import path
from . import views

urlpatterns = [
    path('api/shows', views.ShowList.as_view(), name='show_list'),
    path('api/shows/<int:pk>', views.ShowDetail.as_view(), name='show_detail'),
]