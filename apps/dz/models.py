from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=1)

    def set_price(self, price):
        self.price = price

    def set_name(self, name):
        self.name = name


class Profile(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    balance = models.DecimalField(decimal_places=1)


class Order(models.Model):
    customer = models.ForeignKey(to=Profile, on_delete=models.CASCADE())
    price = models.DecimalField(decimal_places=1)
    amount = models.IntegerField()
    status = models.CharField(max_length=100)

    def set_status(self, status):
        self.status = status


class Courier(models.Model):
    name = models.CharField(max_length=100)
    orders = models.ForeignKey(to=Order, on_delete=models.CASCADE())

    def change_status(self):
        status = input(f'Введиите статус заказа')
        Order.set_status(status)


class Stuff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    order = models.ManyToManyField(to=Order, on_delete=models.CASCADE())

    def new_name(self):
        name = input('Введите новое название')
        Product.set_name(name)

    def new_price(self):
        price = float(input('Введите новую цену'))
        Product.set_price(price)
