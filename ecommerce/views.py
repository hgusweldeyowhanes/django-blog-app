from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import Product, Category1, Brand, Attribute, AttributeValues,ProductImage,Productline
from .serializer import CategorySerializer, BrandSerializer, ProductSerializer,AttributesValuesSerializer,AttributeSerializer, ProductLineSerializer,ProductImageSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset= Category1.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend,  filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    def list(self,request):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many = True)
        return Response(serializer.data)
class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend,  filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    def list(self,request):
        queryset = self.get_queryset()
        serializer = BrandSerializer(queryset, many = True)
        return Response(serializer.data)

class ProductView(viewsets.ModelViewSet):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

     filter_backends = [DjangoFilterBackend,  filters.SearchFilter]
     filterset_fields = ['name']
     search_fields = ['name']

class ProductlineView(viewsets.ModelViewSet):
    queryset = Productline.objects.all()
    serializer_class = ProductLineSerializer

    filter_backends = [DjangoFilterBackend,  filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

class ProductImageView(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_backends = [DjangoFilterBackend,  filters.SearchFilter]
    filterset_fields = ['name', 'product_line']
    search_fields = ['name', 'product_line']

class AttributeView(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

    def create(self, request, *args ,**kwargs):
        serializer = self.get_serializer(data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
        serializer.is_valid(raise_exception = True)
        return super().create(request,*args, **kwargs)
            

class AttributevalueView(viewsets.ModelViewSet):
    queryset = AttributeValues.objects.all()
    serializer_class = AttributesValuesSerializer

   

     