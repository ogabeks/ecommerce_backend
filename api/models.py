from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    amount = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    category = models.ForeignKey(
        Category, on_delete=models.SET_DEFAULT, default="Unknown")
    delivery = models.BooleanField()
    cover1 = models.ImageField(upload_to="product_covers/")
    cover2 = models.ImageField(upload_to="product_covers/")
    cover3 = models.ImageField(upload_to="product_covers/")
    cover4 = models.ImageField(upload_to="product_covers/")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    stars = models.IntegerField(default=1, validators=[
                                MaxValueValidator(5), MinValueValidator(1)])
    sold = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    discount = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product)
    customer = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default="Unknown")
    is_completed = models.BooleanField()
    is_paid = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
