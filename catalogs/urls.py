from django.urls import path
from .views import create_catalog

app_name = 'catalogs'
urlpatterns = [
    path('create/', create_catalog, name='create')
]
