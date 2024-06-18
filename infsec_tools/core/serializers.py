from rest_framework import serializers
from .models import Classifier, Complexsolution, Complexsolutionproducts, Customerrequest, Customerrequestitems, Employee, Product, Soldproduct

class ClassifierSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Classifier """
    class Meta:
        model = Classifier
        fields = '__all__'

class ComplexsolutionSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Complexsolution """
    class Meta:
        model = Complexsolution
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Product """
    class Meta:
        model = Product
        fields = '__all__'

class ComplexsolutionproductsSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Complexsolutionproducts """
    class Meta:
        model = Complexsolutionproducts
        fields = '__all__'

class CustomerrequestSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Customerrequest """
    class Meta:
        model = Customerrequest
        fields = '__all__'

class CustomerrequestitemsSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Customerrequestitems """
    class Meta:
        model = Customerrequestitems
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Employee """
    class Meta:
        model = Employee
        fields = '__all__'

class SoldproductSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Soldproduct """
    class Meta:
        model = Soldproduct
        fields = '__all__'