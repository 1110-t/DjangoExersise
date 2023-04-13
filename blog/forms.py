from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','author','text')
        labels = {
            'title': 'タイトル',
            'author': '著者',
            'text': '記事内容',
        }
        