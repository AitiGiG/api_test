from django.urls import path
from .views import *

urlpatterns = [
    path('get/', get_products),
    path('create/', create_product),
    path('get/<int:pk>/', get_one_product),
    path('update/<int:pk>/' , update_product),
    path('delete/<int:pk>/', delete_product),
    path('<int:pk>/', detail)
]
