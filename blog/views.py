from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from .models import Article
from .forms import ArticleForm

# Create your views here.
def blogs(request):
    articles = Article.objects.all()
    context = {"articles":articles}
    return render(request,'blog/index.html',context)
def blog(request,pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/blog.html', {'article': article})
def new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('/')
    else:
        form = ArticleForm()
    return render(request, 'blog/edit.html', {'CRUD':'登録','form': form})
def edit(request,pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('edit', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    params = {"form":form,'CRUD':'編集'}
    return render(request, 'blog/edit.html', params)
def delete(request,pk):
    if request.method == "POST":
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('/')
def users(request):
    users = User.objects.all() # ユーザーをすべて取得する
    context = {"users":users} # ユーザーを全て表示する
    return render(request,'blog/users.html',context)
def user(request,pk):
    user = get_object_or_404(User, pk=pk)
    articles = Article.objects.filter(author=pk)
    print(articles)
    return render(request, 'blog/user.html', {'user': user,'articles':articles})