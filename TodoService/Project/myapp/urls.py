from django.urls import path
from .views import TodoView

urlpatterns = [
    path('item/', TodoView.as_view()),
]