from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('info/', views.info, name='info'),
    path('register/', views.register, name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='home'), name='logout'),
]
