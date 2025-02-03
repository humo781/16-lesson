from django.urls import path
from .views import create_color

app_name = 'colors'
urlpatterns = [
    path('create/', create_color, name='create')
]
