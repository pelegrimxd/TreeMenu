from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reviews/', views.reviews, name='reviews'),
    path('products/', views.home, name='products'),
    path('products-category/', views.products_category, name='products_category'),
    path('under-home/', views.under_home, name='under_home'),
    path('dunder-home/', views.dunder_home, name='dunder_home'),
]
