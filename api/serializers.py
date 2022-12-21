from rest_framework import serializers
from .models import Product, Category, Order
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "cover1", "cover2", "cover3", "cover4", "slug", "amount", "category",
                  "delivery", "price", "stars", "sold", "discount", "created_at", "updated_at"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "email", "password"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
