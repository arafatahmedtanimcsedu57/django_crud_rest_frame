from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name='products_views'),
    path('<int:id>', views.ProductView.as_view(), name='product_views')
]
