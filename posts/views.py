from django.shortcuts import render
from django.http import HttpResponse
import random
from posts.models import Post

def main_view(request):
    return render(request, 'base.html')



def hello_view(request):
    return HttpResponse(f"Hello World! {random.randint(1,100)}" )


def html_view(request):
    return render(request, "base.html")


def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})

class Template():
    def __init__(self, context: dict = {}) -> None:
        self.context = context

        def display(self):
            if self.context:
                return self.context.items()
            else:
                return None

