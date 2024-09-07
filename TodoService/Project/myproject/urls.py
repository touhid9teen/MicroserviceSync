from django.urls import path, include

urlpatterns = [
    path('todo/', include('myapp.urls')),
]
