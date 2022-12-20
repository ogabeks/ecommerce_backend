from django.urls import path
from .views import ProductsListAPI, CategoryListAPI, MyTokenObtainPairView, UsersAPI
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("products/", ProductsListAPI.as_view(), name="products"),
    path("categories/", CategoryListAPI.as_view(), name="categories"),
    path("user/", UsersAPI.as_view(), name="user"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
