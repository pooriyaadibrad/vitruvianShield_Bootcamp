from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getUser/<int:pk>', views.get_user, name='getData'),
]
