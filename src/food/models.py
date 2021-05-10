from django.db import models

class FoodCategory(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.title


class Food(models.Model):
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=512, blank=False, null=False)
    slug = models.SlugField(blank=True, unique=True)
    photo = models.TextField(blank=True, )
    price = models.FloatField(default=0.00, blank=True)
    ratio = models.CharField(max_length=50, default='1:1', blank=False, null=False)
    is_active = models.BooleanField(default=True, blank=True)
    ordered_in_restaurant = models.IntegerField(default=0, blank=True)
    ordered_in_home = models.IntegerField(default=0, blank=True)


    class Meta:
        db_table = 'foods'

    def __str__(self):
        return self.category.title
