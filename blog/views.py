from django.shortcuts import render
from .models import User

# Create your views here.
def users(request):
    users = User.objects.all() # ユーザーをすべて取得する
    context = {"users":users} # ユーザーを全て表示する
    return render(request,'katachi/user.html',context)