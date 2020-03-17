from django.shortcuts import render
from .models import Post, Comment
from .forms import AddPost, AddComment

# Create your views here.
#forum homepage
#addpost page
#viewpost page- add comment

def forum_page(request):
    posts = Post.objects.all()
    return render(request, 'forum/homepage.html', {'boots': posts})

def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'forum/show_post.html', {'boot': post})

def add_post(request):
    if request.method == 'POST':
        Form = AddPost