from rest_framework import serializers
from .models import Post, Comment,Category
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']

    

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username','email','password','password2','first_name','last_name']
        extrra_kwargs = {
            'password':{"write_only":True},
            'password2':{"write_only":True}

        }

    def validate(self, data):
        if data['password']!= data['password2']:
            raise serializers.ValidationError('Password must match')
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = "__all__"



class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    categories =  CategorySerializer(read_only = True, many= True)
    comments  = CommentSerializer(read_only = True, many = True)
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['author']

