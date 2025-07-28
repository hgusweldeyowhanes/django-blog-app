from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet,CommentViewSet, CategoryViewSet, CustomUserRegistration


router = DefaultRouter()
router.register(r'posts',PostViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'categories',CategoryViewSet)
# router.register(r'register',CustomUserRegistration, basename='register')


urlpatterns = [
    path('', include(router.urls)),
    path('register/',CustomUserRegistration.as_view(), name='register' )

]