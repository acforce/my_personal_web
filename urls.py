from django.conf.urls import url
from django.views.generic.dates import DateDetailView
from django.views.generic.dates import ArchiveIndexView

from . import views
from weblog.models import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', DateDetailView.as_view(month_format='%m', model=Entry, date_field="pub_date"), name='entry_detail'),
    url(r'^tag/(?P<tag_name>[ \w]+)/$', views.get_entries_by_tag, name='tag'),
    url(r'^category/(?P<category_name>[ \w]+)/$', views.get_entries_by_category, name='category'),
    url(r'^home/$', views.index, name='home'),
    url(r'^home/page/(?P<page_number>[0-9]+)/$', views.home, name='home'),
]

