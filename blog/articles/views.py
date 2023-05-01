from .models import Article
from django.shortcuts import render

def archive(request):
    posts = Article.objects.all()
    context = {'posts': posts}
    return render(request, 'archive.html', {"posts": Article.objects.all()})

# Create your views here.
