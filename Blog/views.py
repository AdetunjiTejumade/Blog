from django.shortcuts import render, get_object_or_404,redirect
from .models import post, Comment
from django.core.paginator import Paginator
from .form import CommentForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.

def blog_view(request):
    posts = post.objects.all()   

    paginator = Paginator(posts, 4)

    page = request.GET.get('page')
    contact = paginator.get_page(page)
    
    context = {
        'post':contact 
    }
    return render(request, 'index.html', context)

def detail_view(request,blog_id):
    blog_detail = get_object_or_404(post,pk=blog_id)
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST or  None)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                text = form.cleaned_data["text"],
                post = blog_detail
            )
            comment.save()
            form = CommentForm() #re render the form after submit
        else:
            form = CommentForm(request.POST)

        
    comments = Comment.objects.filter(post=blog_detail)
    context = {
        'blog': blog_detail,
        'comments':comments,
        'form':form,
    }
    return render(request, 'post.html', context)

# def post_remove(request, blog_id):
#     posts = get_object_or_404(post, pk=blog_id)
#     posts.delete()
#     return redirect('/')

def post_remove(request, blog_id):
     posts = get_object_or_404(post, pk=blog_id)
     if request.method == "POST":
        posts.delete()
        return redirect('/')
     context = {
        'objects': 'posts'
     }
     return render(request, 'confirm.html', context)
