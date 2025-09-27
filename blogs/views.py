from django.shortcuts import render,redirect
from .models import Blog,Post
from .forms import Blogform,Postform
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def index(request):
    return render(request,'blogs/index.html')

def blogs(request):
    blogi = Blog.objects.order_by('date_added')
    context = {'blogi' : blogi }
    return render(request,'blogs/blogs.html',context)

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    posty = blog.post_set.all()
    context = {'posty' : posty , 'blog' : blog}
    return render(request,'blogs/blog.html',context)

@login_required
def new_blog(request):
    if request.method != "POST":
        form = Blogform()
    else:
        form = Blogform(data=request.POST)
        if form.is_valid():
            form.save()
            # do something.
            return redirect('blogs:blogs')
    context = {'form': form}
    return render(request, "blogs/new_blog.html", context)

@login_required
def new_post(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method != "POST":
        form = Postform()
    else:
        form = Postform(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:blog',blog_id = blog_id)
    context = {'form': form,'blog': blog}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request,post_id):
    post = Post.objects.get(id=post_id)
    check_post_owner(post.owner,request.user)
    blog = post.blog
    if request.method != "POST":
        form = Postform(instance=post)
    else:
        form = Postform(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog',blog_id = blog.id)
    context = {'form' : form,'post' : post ,'blog' : blog}
    return render(request, 'blogs/edit_post.html', context)


def edit_blog(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method != "POST":
        form = Blogform(instance=blog)
    else:
        form = Blogform(instance=blog,data=request.POST)
        if form.is_valid():
            form.save()
            # do something.
            return redirect('blogs:blog',blog_id = blog_id)
    context = {'form': form,'blog': blog}
    return render(request, "blogs/edit_blog.html", context)

def check_post_owner(owner,user):
    if owner!=user:
        raise Http404