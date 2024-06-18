from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import home, product_list, product_detail, complexsolution_list, complexsolution_detail

router = DefaultRouter()

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('complexsolutions/', complexsolution_list, name='complexsolution_list'),
    path('complexsolutions/<int:pk>/', complexsolution_detail, name='complexsolution_detail'),
    path('api/', include(router.urls)),
]