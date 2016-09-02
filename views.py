import math

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import *
# Create your views here.

def index(request):
    latest_entries = Entry.objects.order_by('-pub_time')[0:5]
    tags = Tag.objects.all()
    categories = Category.objects.all()
	
    context = {
        'latest_entries': latest_entries,
        'tags': tags,
        'categories': categories,
        'page_number': 1,
    }
    return render(request, 'weblog/home.html', context)

def home(request, page_number):
    entry_count = len(Entry.objects.all())
    page_count = math.ceil(1.0*entry_count/5)
    page_number = int(page_number)
    if page_number < 1 or page_number > page_count:
        raise Http404("invalid page number!")
    lower = (page_number-1)*5
    upper = lower+5
    latest_entries = Entry.objects.order_by('-pub_time')[lower:upper]
    tags = Tag.objects.all()
    categories = Category.objects.all()

    context = {
        'latest_entries': latest_entries,
        'tags': tags,
        'categories': categories,
        'page_number': page_number,
    }
    return render(request, 'weblog/home.html', context)

def article(request, year, month, day, slug):
    return HttpResponse(slug)

def get_entries_by_tag(request, tag_name):
    entries = Entry.objects.filter(tags__name=tag_name).order_by('-pub_time')[0:10]
    tags = Tag.objects.filter(name=tag_name)
    categories = Category.objects.all()
    context = {
        'entries': entries,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'weblog/tag_list.html', context)

def get_entries_by_category(request, category_name):
    entries = Entry.objects.filter(categories__name=category_name).order_by('-pub_time')[0:10]
    tags = Tag.objects.all()
    categories = Category.objects.filter(name=category_name)
    context = {
        'entries': entries,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'weblog/category_list.html', context)


