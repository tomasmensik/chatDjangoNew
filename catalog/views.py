from django.shortcuts import render
from .models import User, Room, Message
from django.views import generic

def index(request):

    num_users = User.objects.all().count()
    num_rooms = Room.objects.all().count()
    num_messages = Message.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_users': num_users,
        'num_rooms': num_rooms,
        'num_messages': num_messages,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)



class UserListView(generic.ListView):
    model = User
    context_object_name = 'user_list'
    # queryset = User.objects.filter(name__icontains='a')[:5]
    template_name = 'users/user_list.html'

class UserDetailView(generic.DetailView):
    model = User
    context_object_name = 'userDetail'
    template_name = 'catalog/user_detail.html'


class RoomListView(generic.ListView):
    model = Room
    context_object_name = 'room_list'
    # queryset = Room.objects.filter(title__icontains='a')[:5]
    template_name = 'rooms/room_list.html'

class RoomDetailView(generic.DetailView):
    model = Room
    context_object_name = 'roomDetail'
    template_name = 'room_detail.html'

class MessageListView(generic.ListView):
    model = Message
    context_object_name = 'message_list'
    # queryset = Message.objects.filter(title__icontains='a')[:5]
    template_name = 'messages/message_list.html'

class MessageDetailView(generic.DetailView):
    model = Message
    context_object_name = 'messageDetail'
    template_name = 'message_detail.html'