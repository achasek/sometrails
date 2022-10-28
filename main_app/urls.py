from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.auth, name='auth'),
    path('/index/', views.index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('hikes/create/', views.HikeCreate.as_view(), name='hikes_create'),
    path('accounts/login', auth_views.LoginView.as_view(
        template_name='login.html',
        extra_context={
            'next': '/hikes/index',
        },
    ), name='login'),
]
