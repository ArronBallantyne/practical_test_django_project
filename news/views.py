from django.http import HttpResponse
from django.shortcuts import render
from news.models import NewsArticle
from django.template import loader

def news(request):

    latest_article_list = NewsArticle.objects.order_by('-publication_date')[:5]
    template = loader.get_template('news/newspage.html')

    context = {
        'latest_article_list': latest_article_list,
    }

    return render(request, 'news/newspage.html',context)
