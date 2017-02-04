from django.shortcuts import render

# Create your views here.

from .models import Authors
from .models import Articles


def index(request):
    authors = Authors.objects.order_by('-rate')
    context = {
        'authors': authors
    }
    return render(request, 'articles/index.html', context)

def author(request, author_id):
    author = Authors.objects.filter(id=author_id)[0]
    articles = Articles.objects.filter(author__id=author_id).order_by('-pub_date')
    context = {
        'author': author,
        'articles': articles,
    }
    return render(request, 'articles/author.html', context)


