# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Classifier(models.Model):
    classifier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='Cyrillic_General_CI_AS')
    description = models.TextField(db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Classifier'


class Complexsolution(models.Model):
    solution_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='Cyrillic_General_CI_AS')
    description = models.TextField(db_collation='Cyrillic_General_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ComplexSolution'

    def get_products(self):
        return Product.objects.filter(complexsolutionproducts__solution=self)


class Complexsolutionproducts(models.Model):
    solution = models.ForeignKey(Complexsolution, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ComplexSolutionProducts'


class Customerrequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100, db_collation='Cyrillic_General_CI_AS')
    request_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'CustomerRequest'


class Customerrequestitems(models.Model):
    request = models.ForeignKey(Customerrequest, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, blank=True, null=True)
    solution = models.ForeignKey(Complexsolution, on_delete=models.SET_NULL, blank=True, null=True)
    quantity_solution = models.IntegerField()
    quantity_product = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'CustomerRequestItems'
        unique_together = (('request', 'product', 'solution'), ('request', 'product', 'solution'),)


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='Cyrillic_General_CI_AS')
    role = models.CharField(max_length=50, db_collation='Cyrillic_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'Employee'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='Cyrillic_General_CI_AS')
    description = models.TextField(db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    classifier = models.ForeignKey(Classifier, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Product'


class Soldproduct(models.Model):
    sold_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    sale_date = models.DateField()
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'SoldProduct'

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Корзина {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    solution = models.ForeignKey(Complexsolution, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        if self.product:
            return f'{self.quantity} x {self.product.name}'
        elif self.solution:
            return f'{self.quantity} x {self.solution.name}'
        else:
            return 'Корзина без продуктов и решений'
    
    def total_price(self):
        if self.product:
            return self.quantity * self.product.price
        elif self.solution:
             # Суммируем цены продуктов, входящих в комплексное решение
            products = self.solution.complexsolutionproducts_set.all()
            total_price = sum(product.product.price * self.quantity for product in products)
            return total_price
        else:
            return 0