from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('registration/', views.RegisterUserView.as_view(), name='registration'),
    path('profile/', views.ProfileView.as_view(), name= "profile")
]
