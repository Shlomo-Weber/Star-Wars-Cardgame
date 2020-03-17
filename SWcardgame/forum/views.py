from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
# Create your views here.




#forum homepage
def forum_page(request):
    posts = Post.objects.all()
    return render(request, 'forum/homepage.html', {'posts': posts})

#viewpost page- add comment
def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('Forum')
    else:
        form = CommentForm()
    return render(request, 'forum/show_post.html', {'boot': post, 'form': form})

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


# def post_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})

# post = Post.objects.get(id=post_id)
#     if request.method =='POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#            comment=form.save(commit=False)
#            comment.post= post
#            comment.save()
#     else:
#         form = CommentForm()
#     return render(request, 'forum/show_post.html', {'boot': post, 'form':form})