from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('info/', views.UserInfoView.as_view()),
    path('public-key/', views.PublicKeyView.as_view(), name='public_key')
]
