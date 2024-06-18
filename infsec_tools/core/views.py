from rest_framework import viewsets
from .models import Classifier, Complexsolution, Complexsolutionproducts, Customerrequest, Customerrequestitems, Employee, Product, Soldproduct, Cart, CartItem

from django.shortcuts import redirect, render
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

def add_to_cart(request, product_id=None, solution_id=None):
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if product_id:
        product = get_object_or_404(Product, product_id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    elif solution_id:
        solution = get_object_or_404(Complexsolution, solution_id=solution_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, solution=solution)
    
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart_detail')

def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'core/cart_detail.html', {'cart': cart})
