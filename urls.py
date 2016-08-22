from django.conf.urls import url
from django.views.generic.dates import DateDetailView
from django.views.generic.dates import ArchiveIndexView

from . import views
from weblog.models import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', DateDetailView.as_view(month_format='%m', model=Entry, date_field="pub_date"), name='entry_detail'),
]

