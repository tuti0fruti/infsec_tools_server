from rest_framework import viewsets
from .models import Classifier, Complexsolution, Complexsolutionproducts, Customerrequest, Customerrequestitems, Employee, Product, Soldproduct
from .serializers import ClassifierSerializer, ComplexsolutionSerializer, ComplexsolutionproductsSerializer, CustomerrequestSerializer, CustomerrequestitemsSerializer, EmployeeSerializer, ProductSerializer, SoldproductSerializer

class ClassifierViewSet(viewsets.ModelViewSet):
    """ Представление для модели Classifier """
    queryset = Classifier.objects.all()
    serializer_class = ClassifierSerializer

class ComplexsolutionViewSet(viewsets.ModelViewSet):
    """ Представление для модели Complexsolution """
    queryset = Complexsolution.objects.all()
    serializer_class = ComplexsolutionSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """ Представление для модели Product """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ComplexsolutionproductsViewSet(viewsets.ModelViewSet):
    """ Представление для модели Complexsolutionproducts """
    queryset = Complexsolutionproducts.objects.all()
    serializer_class = ComplexsolutionproductsSerializer

class CustomerrequestViewSet(viewsets.ModelViewSet):
    """ Представление для модели Customerrequest """
    queryset = Customerrequest.objects.all()
    serializer_class = CustomerrequestSerializer

class CustomerrequestitemsViewSet(viewsets.ModelViewSet):
    """ Представление для модели Customerrequestitems """
    queryset = Customerrequestitems.objects.all()
    serializer_class = CustomerrequestitemsSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """ Представление для модели Employee """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SoldproductViewSet(viewsets.ModelViewSet):
    """ Представление для модели Soldproduct """
    queryset = Soldproduct.objects.all()
    serializer_class = SoldproductSerializer