from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
from posts.models import Post
from posts.forms import PostForm

def hello_view(request):
    return HttpResponse(f"Hello World! {random.randint(1,100)}" )


def html_view(request):
    return render(request, "base.html")

def main_view(request):
    if request.method == 'GET':
        return render(request, 'base.html')


def posts_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, "posts/post_list.html", context={"posts": posts})

def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        return render(request, "posts/post_detail.html", context={"post": post})

def post_create_view(request):
    if request.method == 'GET':
        form= PostForm()
        return render(request, "posts/post_create.html", context={"form":form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if  not form.is_valid():
            return render(request, "posts/post_create.html", context={"form":form})
        elif form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
        post = Post.objects.create(title=title, description=description, image=image)
        return redirect("/posts/")



