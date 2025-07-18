from rest_framework.routers import DefaultRouter

# Import ViewSets
from users.views import UserViewSet, AddressViewSet
from products.views import CategoryViewSet, ProductViewSet
from cart.views import CartViewSet
from reviews.views import ReviewViewSet
# from orders.views import 

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'reviews', ReviewViewSet, basename='review')
