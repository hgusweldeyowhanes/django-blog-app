from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.utils.timezone import now
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Room,Topic, Message,RoomVisit,Poll,Vote,choice, User
from .forms import RoomForm,PollForm, choiceForm
from django.contrib.auth import get_user_model

User = get_user_model()

def LoginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('product:home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username):
            messages.error(request, 'User Does not Exist')
        else:
            user = authenticate(request, username= username, password = password)
            if user is not None:
                login(request, user)
                return redirect('product:home')
            else:
                messages.error(request, 'Inccorect password not Exist')
    context = {'page':page}
    return render(request , 'product/login_register.html', context)
def LogOut(request):
    logout(request)
    return redirect('product:home')

def Register(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('product:home')
        else:
           messages.error(request, 'Error occurred during registration')   
        
    return render(request, 'product/login_register.html', {'form':form , 'page':page})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains =q) |
                                Q(name__icontains=q) |
                                Q(description__icontains=q) )
    topics = Topic.objects.all()[0:5]
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains =q))
    context = {'rooms': rooms,'topics':topics, 'room_count': room_count,'room_messages':room_messages}
    return render(request , 'product/home.html', context)

def room(request, pk):
    room = Room.objects.get(id =pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('product:room', pk = room.id)
    if request.user.is_authenticated:
        visit, created = RoomVisit.objects.get_or_create(user = request.user, room = room)
        visit.last_visited = now()
        visit.save()
        recent_visit = RoomVisit.objects.filter(user = request.user).order_by('-last_visited')[:5]
    context = {'room':room,
               'room_messages':room_messages,  
               'participants':participants,
               'recent_visit':recent_visit}
    return render(request, 'product/room.html', context)
def userProfile(request,pk):
    user = User.objects.get(id = pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user':user, 'rooms': rooms ,'room_messages':room_messages, 'topics':topics}
    return render(request ,'product/profile.html', context)

@login_required(login_url='/accounts/login/')
def createRoom(request):
     form = RoomForm()
     topics = Topic.objects.all()
     if request.method == 'POST':
         topic_name = request.POST.get('topic')
         topic, created = Topic.objects.get_or_create(name = topic_name)
         Room.objects.create(host = request.user, topic = topic,
                             name = request.POST.get('name'),
                             description = request.POST.get('description'),
                             )
         return redirect('product:home')
     context ={'form': form, 'topics':topics}
     return render(request, 'product/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse('You are not allowed here!')
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name = topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')
        

    context = {'form': form,'room':room ,'topics':topics}
    return render(request, 'product/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.user != room.host:
        return HttpResponse('you are not allowed')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'product/delete.html',{'obj': room})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message= Message.objects.get(id = pk)
    if request.user != message.user:
        return HttpResponse('You are not allowed to delete')
    if request.method == 'POST':
        message.delete()
        return redirect('product:home')
    return render(request, 'product/delete.html',{'obj': message})

@login_required(login_url='login')
def updateMessage(request, pk):
    message = get_object_or_404(Message, pk = pk)

    if request.user != message.user:
        return redirect('product:room', pk = message.room.id)
    if request.method == 'POST':
        new_body = request.POST.get('body')
        if new_body:
            message.body = new_body
            message.save()
            return redirect('product:room', pk = message.room.id)

    context = {'message': message}
    return render(request, 'product/edit_message.html', context)

@login_required
def RoomDetail(request,pk):
    room = Room.objects.all(id =pk)
    if request.user.is_authenticated:
        visit = RoomVisit.objects.get_or_create(user = request.user, room = room)
        visit.last_visited = now()
        visit.save()
    context = {
        'room':room,
        'recent_visit':RoomVisit.objects.filter(room=room).order_by('-last_visited')[:10]
    }
    return render(request,'product/room.html' , context)
@login_required
def RoomPoll(request,poll_id):
    poll = get_object_or_404(Poll,id =poll_id)
    choices = poll.choices.all()
    voted = Vote.objects.filter(user=request.user, choice__poll=poll).exists()

    context = {'poll':poll,
               'choices':choices,
               'voted':voted}
    return render(request, 'product/poll.html',context)

@login_required
def Vote_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        selected_choice = get_object_or_404(choice, id=choice_id, poll=poll)

        existing_vote = Vote.objects.filter(user=request.user, choice__poll=poll)
        if existing_vote.exists():
            existing_vote.delete()

        Vote.objects.create(user=request.user, choice=selected_choice)
        return redirect('product:poll', poll_id=poll.id)
    choices = poll.choices.all()
    voted = Vote.objects.filter(user=request.user, choice__poll= poll).exists()
    context = {
        "poll":poll,
        "choices":choices,
        "voted":voted
    }

    return render(request,'product/poll.html', context)

def pollFormView(request):  
    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        if poll_form.is_valid():
            poll = poll_form.save(commit=False)
            poll.created_by = request.user
            poll.save()
            # Create 3 choices
            for i in range(1, 4):
                text = request.POST.get(f'choice{i}')
                if text:
                    choice.objects.create(poll=poll, text=text)
            return redirect('product:poll', poll_id=poll.id)  
    else:
        poll_form = PollForm() 

    return render(request, 'product/create_poll.html', {'form': poll_form})


@login_required(login_url='login')    
def userUpdate(request):
    user = request.user
    form = CustomUserCreationForm(instance=user)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('product:user-profile', pk = user.id)
    
    return render(request ,'product/user-update.html' ,{'form':form})

def topicPage(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    topics = Topic.objects.filter(name__istartswith=q) 
    context = {'topics': topics}
    return render(request, 'product/topics.html', context)

def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'product/activity.html', {'room_messages': room_messages})
