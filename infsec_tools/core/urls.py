from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import add_to_cart, cart_detail, home, product_list, product_detail, complexsolution_list, complexsolution_detail, remove_from_cart

router = DefaultRouter()


urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('complexsolutions/', complexsolution_list, name='complexsolution_list'),
    path('complexsolutions/<int:pk>/', complexsolution_detail, name='complexsolution_detail'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/product/<int:product_id>/', add_to_cart, name='add_to_cart_product'),
    path('cart/add/solution/<int:solution_id>/', add_to_cart, name='add_to_cart_solution'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('api/', include(router.urls)),
]