from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(request):
    latest_entries = Entry.objects.order_by('-pub_time')[0:10]
    tags = Tag.objects.all();
    categories = Category.objects.all();
	
    context = {
        'latest_entries': latest_entries,
	    'tags': tags,
	    'categories': categories,
    }
    return render(request, 'weblog/home.html', context)

def article(request, year, month, day, slug):
    return HttpResponse(slug)


# Create your views here.

