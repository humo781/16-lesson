from django.urls import path
from .views import create_brand

app_name = 'brands'
urlpatterns = [
    path('create/', create_brand, name='create')
]
