from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse

from .models import Blog, Author, Entry
# Create your views here.

def index(request):
    latest_entries = Entry.objects.order_by('-pub_time')[0:10]
    context = {
        'latest_entries': latest_entries,
    }
    return render(request, 'weblog/home.html', context)

def article(request, year, month, day, slug):
    return HttpResponse(slug)

=======

# Create your views here.
>>>>>>> bf50107ea9289371f0c23b17355ca7316f414783
