from django.db import models
from food.models import Food
from base.models import BaseModel


class RestaurantManager(models.Manager):
    def all(self):
        return self.filter(is_active=True)


class Restaurant(BaseModel):
    # Basic
    title = models.CharField(max_length=500, blank=False, null=False)
    slug = models.SlugField(blank=True, unique=True)
    phone = models.CharField(max_length=128, blank=False, null=False)
    email = models.CharField(max_length=252, blank=True, null=True, default='')
    # minimum
    min_serve_time = models.IntegerField(default=30, blank=False, verbose_name='Minimum Serve Time')
    min_order_tk = models.FloatField(default=150.00, blank=False, verbose_name='Minimum Order')
    service_charge = models.FloatField(default=30.00, blank=False, verbose_name='Service Charge')
    vat_tax = models.FloatField(default=0.0, blank=True, verbose_name='Vat/Tax')
    # location/contact
    city = models.CharField(max_length=128, default='', blank=True)
    address = models.CharField(max_length=1024, blank=False, null=False)
    environment = models.CharField(max_length=512, blank=False, null=False)
    map_embed_url = models.TextField(blank=False, default='https://maps.google.com/')

    # Others
    is_active = models.BooleanField(default=False)
    is_orderable = models.BooleanField(default=False)
    extra_info = models.TextField(blank=True, null=True)
    food_items = models.ManyToManyField(Food, blank=True)
    # Restaurant qs manager
    objects = RestaurantManager()

    def __str__(self):
        return self.title


