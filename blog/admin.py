from django.contrib import admin
from .models import Post,Comment,Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','status','author','publish_date')
    list_filter = ('title','content','publish_date')
    search_fields = ('title','content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author', 'content','created_date','approved')
    list_filter = ('approved','created_date')
    search_fields = ('name','email','body')
    actions = ['approved_cooment']

    def approved(self,request, queryset):
        queryset.update(approved = True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name']
    list_filter = ['name']
    search_fields = ['name']
    