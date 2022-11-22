from django.urls import path
from . import views

app_name = "profilepage"

urlpatterns = [
    # path('', views.profile_list, name='profile_list'),
    path('', views.profileMapView.as_view()),
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:pk>/edit/', views.profile_edit, name='profile_edit'),
]
