from django.urls import path
from . import views

urlpatterns = [
    path('', views.profileMapView.as_view(), name="profile_list"),
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:pk>/edit/', views.profile_edit, name='profile_edit'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
