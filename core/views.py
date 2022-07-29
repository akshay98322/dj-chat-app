from django.shortcuts import render
from .models import Chat, Group


def index(request, group_name):
    print(f"Group Name: {group_name}")
    group, created = Group.objects.get_or_create(name=group_name)
    chats = Chat.objects.filter(group=group)
    context = {'groupname': group_name, 'chats': chats}
    return render(request, 'core/index.html', context)
