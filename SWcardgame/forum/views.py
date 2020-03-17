from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
# Create your views here.




#forum homepage
def forum_page(request):
    posts = Post.objects.all()
    return render(request, 'forum/homepage.html', {'boots': posts})

#viewpost page- add comment
def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'forum/show_post.html', {'boot': post})

#addpost page

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('Forum')
    else:
        form = PostForm()
        return render(request, 'forum/add_post.html',{'form':form})
