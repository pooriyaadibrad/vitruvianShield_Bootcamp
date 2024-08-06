from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getUser/<int:pk>', views.get_user, name='getData'),
    path('deleteUser/<int:pk>', views.delete_user, name='deleteUser'),
]
