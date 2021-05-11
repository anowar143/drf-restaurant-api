from django.db import models
from user.models import User
from food.models import Food
from restaurant.models import Restaurant

from base.models import BaseModel

PAYMENT_METHODS = (
    ('pod', 'Pay On Delivery'),
    ('bkash', 'bKash'),
    ('dbbl', 'DBBL'),
)

DELIVERY_TYPES = (
    ('home', 'Home'),
    ('restaurant', 'Restaurant')
)


class Cart(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True)
    key = models.CharField(max_length=128, blank=True, default='')
    products = models.ManyToManyField(Food, blank=True)
    quantities = models.CharField(max_length=512, default='', blank=True)
    subtotal = models.FloatField(default=0.00, blank=True)
    total = models.FloatField(default=0.00, blank=True)
    is_active = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.restaurant.title + ' - ' + str(self.total)


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    order_id = models.CharField(blank=True, max_length=256, default='')
    order_no = models.CharField(blank=True, max_length=256, default='')
    name = models.CharField(max_length=100, default='', blank=False)
    phone = models.CharField(max_length=20, default='', blank=False)
    shipping_address = models.CharField(max_length=200, default='', blank=False)
    status = models.BooleanField(default=False, blank=True)
    payment_status = models.BooleanField(default=False, blank=True)
    shipping_charge = models.FloatField(default=30.00, blank=True)
    order_type = models.CharField(max_length=100, default='home', blank=False, choices=DELIVERY_TYPES)
    payment_method = models.CharField(max_length=100, default="pod", choices=PAYMENT_METHODS)
    expected_time = models.TimeField(blank=True, null=True, default='')
    discount = models.FloatField(default=0.00, blank=True)
    cost = models.FloatField(default=0.00, blank=True)
    is_active = models.BooleanField(default=True, blank=True)


    def __str__(self):
        return self.name + " - " + self.phone + " - " + self.shipping_address + " - " + str(self.cost)


class Discount(models.Model):
    percentage = models.FloatField(default=0.00, blank=True)
    key = models.CharField(max_length=100, blank=True, default='')
    used = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.percentage) + " - " + str(self.used)

