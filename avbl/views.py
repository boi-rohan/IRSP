from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>avlb app homepage</h1>")


def detail(request, court_id):
    return HttpResponse("<h1>This is court number :  " + str(court_id) + "</h1>")
