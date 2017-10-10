from django.shortcuts import render
from django.utils import timezone
from .models import Post, Link

def getLink(request):
    links = Link.objects.all()
    return render(request, 'deputado/post_list.html', {'link': links})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('nome_deputado')
    return render(request, 'deputado/post_list.html', {'posts': posts})

