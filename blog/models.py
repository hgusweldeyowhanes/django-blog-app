from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','draft'),
         ('published','published')
    )
    title = models.CharField(max_length=255)
    content= models.TextField(blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    category = models.ManyToManyField(Category,related_name='posts')
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,choices = STATUS_CHOICES, default='draft')
    def is_published(self):
        return self.status == 'published' and self.publish_date <= timezone.now

    # is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"commented by {self.author} on date {self.post.title}"
    