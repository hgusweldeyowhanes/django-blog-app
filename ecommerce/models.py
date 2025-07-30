from django.db import models
from  mptt.models import MPTTModel, TreeForeignKey

class Category1(models.Model):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete= models.PROTECT, null= True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand ,on_delete=models.CASCADE)
    category = TreeForeignKey(Category1, on_delete= models.SET_NULL, null= True, blank=True)

    def __str__(self):
        return self.name
    
class Productline(models.Model):
    class Meta:
        ordering = ['product']
    price= models.DecimalField(max_digits=10,decimal_places=2)
    sku = models.CharField(max_length=200,blank=True, null=True)
    stock_qty = models.IntegerField()
    product = models.ForeignKey('Product',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} - SKU: {self.sku}"
    
class ProductImage(models.Model):
    name = models.CharField(max_length=200)
    alternative_text = models.CharField(max_length=200)
    url = models.ImageField(upload_to= 'product_image/')
    product_line = models.ForeignKey('Productline', on_delete=models.CASCADE , related_name='images')

    def __str__(self):
        return self.name
    
class Attribute(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class AttributeValues(models.Model):
    value = models.CharField(max_length=200)
    attribute = models.ForeignKey(Attribute , related_name='values',on_delete=models.CASCADE )

    def __str__(self):
        return f"{self.attribute.name}:{self.value}"


