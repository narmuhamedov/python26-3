from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hello_world_view(request):
    return HttpResponse("<h1>Hello This is my first Django Project :)</h1>")


# posts view
def post_view(request):
    post = models.Post.objects.all()
    return render(request, "index.html", {"post_obj": post})
