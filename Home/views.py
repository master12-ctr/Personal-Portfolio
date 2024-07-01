from django.shortcuts import render, redirect
from .forms import UserForm
# Create your views here.

from .models import CustomUser

def user_list(request):
    all_users = CustomUser.objects.all()
    return render(request, 'user/user_list.html', {'user': all_users})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = UserForm()
    return render(request, 'user/add_user.html', {'form': form})


def index(request):
    first_user = CustomUser.objects.first()
    return render(request, 'user/index.html', {'user': first_user})