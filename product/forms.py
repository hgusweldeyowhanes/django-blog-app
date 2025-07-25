from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Poll,choice
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields  = ['room','question']

class choiceForm(ModelForm):
    class Meta:
        model = choice
        fields  = ['text']