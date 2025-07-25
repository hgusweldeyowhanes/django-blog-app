from django.contrib import admin
from .models import Room, Topic,Message, RoomVisit,Poll,choice,Vote,User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(RoomVisit)
admin.site.register(Poll)
admin.site.register(choice)
admin.site.register(Vote)
admin.site.register(User, UserAdmin)




