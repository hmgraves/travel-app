from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations_index, name='index'),
    # path('destinations/<int:destination_id>/', views.destination_detail, name='detail'),
]