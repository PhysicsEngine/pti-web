from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Authors
from .models import Articles


def author(request, author_id):
    author = Authors.objects.filter(id=author_id)[0]
    articles = Articles.objects.filter(author__id=author_id).order_by('-pub_date')
    context = {
        'author': author,
        'articles': articles,
    }
    return render(request, 'articles/author.html', context)


def index(request):
    authors = Authors.objects.order_by('-rate')
    paginator = Paginator(authors, 25)
    page = request.GET.get('page')

    try:
        extacted_authors = paginator.page(page)
    except PageNotAnInteger:
        extacted_authors = paginator.page(1)
    except EmptyPage:
        extacted_authors = paginator.page(paginator.num_pages)
    context = {
        'authors': extacted_authors,
    }
    return render(request, 'articles/author_list.html', context)


