from rest_framework import serializers
from .models import Product, Category1, Brand, Productline,ProductImage,Attribute, AttributeValues

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category1
        fields = ['id','name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id','name']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'

    def create(self,validated_data):
        category_data = validated_data.pop('category')
        brand_data = validated_data.pop('brand')
        brand = Brand.objects.create(**brand_data)
        category = Category1.objects.create(**category_data)
        product = Product.objects.create(brand = brand, category = category ,**validated_data)
        return product
    

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields= '__all__'
    
class ProductLineSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(read_only = True, many = True)
    class Meta:
        model = Productline
        fields = '__all__'

    def create(self, validated_data):
        image_data = validated_data.pop('images',[])
        productline = Productline.objects.create(**validated_data)
        for img in image_data:
            ProductImage.objects.create(productline = productline, **img)
        return productline


class AttributesValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValues
        fields = ['value']

class AttributeSerializer(serializers.ModelSerializer):
    values = AttributesValuesSerializer(many= True)
    class Meta:
        model = Attribute
        fields = ['id','name','values']

    def create(self , validated_data):
        values_data = validated_data.pop('values')
        attribute = Attribute.objects.create(**validated_data)
        for val in values_data:
            AttributeValues.objects.create(attribute = attribute ,**val)
        return attribute

