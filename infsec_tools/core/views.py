from rest_framework import viewsets
from .models import Classifier, Complexsolution, Complexsolutionproducts, Customerrequest, Customerrequestitems, Employee, Product, Soldproduct

from django.shortcuts import render
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'core/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'core/product_detail.html', {'product': product})

def complexsolution_list(request):
    complexsolutions = Complexsolution.objects.all()
    return render(request, 'core/complexsolution_list.html', {'complexsolutions': complexsolutions})

def complexsolution_detail(request, pk):
    solution = get_object_or_404(Complexsolution, pk=pk)
    products = solution.get_products()
    return render(request, 'core/complexsolution_detail.html', {'solution': solution, 'products': products})


