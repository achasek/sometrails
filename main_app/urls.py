from django.urls import path
from . import views

urlpatterns = [
     path('', views.auth, name='auth'),
     path('hikes/', views.hikes_index, name='index'),
     path('accounts/signup/', views.signup, name='signup'),
     path('hikes/create/', views.HikeCreate.as_view(), name='hikes_create'),
     path('hikes/<int:pk>/', views.HikeDetail.as_view(), name='hikes_detail'),
     path('hikes/<int:pk>/update/', views.HikeUpdate.as_view(), name='hikes_update'),
     path('hikes/<int:pk>/delete/', views.HikeDelete.as_view(), name='hikes_delete'),
     path('hikes/<int:hike_id>/favorite/',
          views.add_favorite, name='add_favorite'),
     path('favorites/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
     path('reviews/<int:pk>/delete/',
          views.ReviewDelete.as_view(), name='reviews_delete'),
     path('hikes/<int:hike_id>/add_review/',
          views.add_review, name='add_review'),
     path('hikes/<int:hike_id>/add_photo/', views.add_photo, name='add_photo'),
     path('photos/<int:pk>/delete/',
         views.PhotoDelete.as_view(), name='photos_delete'),
]
