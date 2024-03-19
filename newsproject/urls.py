
from django.urls import path,include

urlpatterns = [
    path('', include('newsapp.urls')),
]
