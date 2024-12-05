from django.shortcuts import render
from django.http import HttpResponse
import random


def hello_view(request):
    return HttpResponse(f"Hello World! {random.randint(1,100)}" )


def html_view(request):
    return render(request, "base.html")

