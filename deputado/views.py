from django.shortcuts import render
from django.utils import timezone
from .models import Post, Link

''' def getLink(request):
    links = Link.objects.all()
    return render(request, 'deputado/post_list.html', {'links': links}) '''

def post_list(request):
    posts = Post.objects.all()
    links = Link.objects.all()
    return render(request, 'deputado/post_list.html', {'posts': posts, 'links': links})

