#product\urls.py
from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
urlpatterns = [
    path('', ProductListView.as_view(), name='productListView'),
    path('<int:pk>', ProductDetailView.as_view(), name='productDetail'),
    path('create/', ProductCreateView.as_view(), name='productCreateView'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='productUpdateView'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='productDeleteView'),

]


