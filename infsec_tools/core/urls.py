from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ClassifierViewSet, ComplexsolutionViewSet, ComplexsolutionproductsViewSet, CustomerrequestViewSet, CustomerrequestitemsViewSet, EmployeeViewSet, ProductViewSet, SoldproductViewSet

router = DefaultRouter()
router.register(r'Classifiers', ClassifierViewSet)
router.register(r'complexsolutions', ComplexsolutionViewSet)
router.register(r'complexsolutionproducts', ComplexsolutionproductsViewSet)
router.register(r'customerrequests', CustomerrequestViewSet)
router.register(r'customerrequestitems', CustomerrequestitemsViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'soldproducts', SoldproductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]