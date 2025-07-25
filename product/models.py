from django.db import models
from django.contrib.auth.models  import AbstractUser,BaseUserManager
from django.db.models.deletion import CASCADE


class User(AbstractUser):

    name = models.CharField(max_length=200, null=True)
    email= models.EmailField(unique=True, null=True)
    bio = models.TimeField(null=True)
    avatar = models.ImageField(null=True ,blank=True, default=  'hgus.jpg')

    REQUIRED_FIELDS = ['email', 'name']
    
    def __str__(self):
        return self.email

class Topic(models.Model):
    name =  models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated=  models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    pinned_message = models.ForeignKey('Message', on_delete=models.SET_NULL, blank=True, null=True,related_name='pinned_in')

    
    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated=  models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.body[0:50]
class RoomVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    last_visited = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'room')
    
    def __str__(self):
        return f'{self.user.username} visited {self.room.name}'
    
class Poll(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
class choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
class Vote(models.Model):
    choice = models.ForeignKey(choice,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

class RoomTag(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


