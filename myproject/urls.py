from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name= 'token_obtain_pair'),
    path('api/token/refrash/', TokenRefreshView.as_view(), name= 'token-refrash'),
    
]
