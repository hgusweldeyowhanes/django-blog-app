from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView, BrandView, ProductView,ProductImageView,ProductlineView,AttributevalueView,AttributeView


router = DefaultRouter()
router.register(r'category1', CategoryView)
router.register(r'brand', BrandView)
router.register(r'product', ProductView)
router.register(r'productline', ProductlineView)
router.register(r'productimage', ProductImageView)
router.register(r'attribute', AttributeView)
router.register(r'attributevalus', AttributevalueView)


urlpatterns = [
    path('', include(router.urls))
]

