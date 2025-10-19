from django.urls import path
import django.urls
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),  # главная страница
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('contacts/', views.contacts, name='contacts'),
]
