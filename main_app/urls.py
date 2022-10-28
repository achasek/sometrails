from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='auth'),
    path('home/', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('hikes/create/', views.HikeCreate.as_view(), name='hikes_create'),
]
