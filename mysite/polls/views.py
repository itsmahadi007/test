from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def student_show(request):
    x=[]
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>Mahadi Hassan Django Tutorials</h1> The digits are {0}".format(x))
    