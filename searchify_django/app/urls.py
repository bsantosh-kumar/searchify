from django.urls import path
from app import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.HomeView.as_view(), name='index'),
]
