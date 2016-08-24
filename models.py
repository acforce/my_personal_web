from __future__ import unicode_literals

from django.db import models

from django.core.urlresolvers import reverse

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_url(self):
        return '/blog/tag/' + self.name + '/'

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_url(self):
        return '/blog/category/' + self.name + '/'

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    pub_date = models.DateField()
    pub_time = models.DateTimeField(auto_now_add=True)
    mod_time = models.DateTimeField()
    authors = models.ManyToManyField(Author)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})

    def get_url(self):
        year = self.pub_date.isoformat()[0:4]
        month = self.pub_date.isoformat()[5:7]
        day = self.pub_date.isoformat()[8:10]
        url = '/blog/'+year+'/'+month+'/'+day+'/'+self.slug
        return url

    def get_tag_list(self):
        return self.tags.all()

    def get_category_list(self):
        return self.categories.all()

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})



# Create your models here.

