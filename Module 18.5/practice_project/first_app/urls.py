from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/pass_change/', views.pass_change, name="pass_change"),
]
