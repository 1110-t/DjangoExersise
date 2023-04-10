from django.shortcuts import render,get_object_or_404
from .models import User

# Create your views here.
def users(request):
    users = User.objects.all() # ユーザーをすべて取得する
    context = {"users":users} # ユーザーを全て表示する
    return render(request,'blog/users.html',context)
def user(request,pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'blog/user.html', {'user': user})