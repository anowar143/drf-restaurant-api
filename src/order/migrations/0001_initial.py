# Generated by Django 3.2 on 2021-05-11 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('key', models.CharField(blank=True, default='', max_length=128)),
                ('quantities', models.CharField(blank=True, default='', max_length=512)),
                ('subtotal', models.FloatField(blank=True, default=0.0)),
                ('total', models.FloatField(blank=True, default=0.0)),
                ('is_active', models.BooleanField(blank=True, default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_created', to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(blank=True, to='food.Food')),
                ('restaurant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField(blank=True, default=0.0)),
                ('key', models.CharField(blank=True, default='', max_length=100)),
                ('used', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('order_id', models.CharField(blank=True, default='', max_length=256)),
                ('order_no', models.CharField(blank=True, default='', max_length=256)),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=20)),
                ('shipping_address', models.CharField(default='', max_length=200)),
                ('status', models.BooleanField(blank=True, default=False)),
                ('payment_status', models.BooleanField(blank=True, default=False)),
                ('shipping_charge', models.FloatField(blank=True, default=30.0)),
                ('order_type', models.CharField(choices=[('home', 'Home'), ('restaurant', 'Restaurant')], default='home', max_length=100)),
                ('payment_method', models.CharField(choices=[('pod', 'Pay On Delivery'), ('bkash', 'bKash'), ('dbbl', 'DBBL')], default='pod', max_length=100)),
                ('expected_time', models.TimeField(blank=True, default='', null=True)),
                ('discount', models.FloatField(blank=True, default=0.0)),
                ('cost', models.FloatField(blank=True, default=0.0)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.cart')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_updated', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
