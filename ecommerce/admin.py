from django.contrib import admin
from .models import Category1,Product,Brand,ProductImage,Productline,Attribute,AttributeValues

admin.site.register(Category1)
admin.site.register(Product)
admin.site.register(Productline)
admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(Attribute)
admin.site.register(AttributeValues)

