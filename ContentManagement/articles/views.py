# Create your views here
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from articles.form import ArticleForm
from django.http import HttpResponse
from articles.models import Article
from django.template import RequestContext
import datetime


def home_page(request):
    articale_list = Article.objects.all()
    context_variables=RequestContext(request,{'list':articale_list})
    return render_to_response('articles.html',locals(),context_variables)


def home(request, article_id = None):
    article_obj = None
    if article_id:
       article_obj = Article.objects.get(id = article_id)
       
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = article_obj)
        if form.is_valid():
            article_form=form.save(commit=False)           
            if article_id:
                article_form.modified_at=datetime.datetime.now()
            article_form.save()
            return HttpResponseRedirect('/')
    else:
        if article_id:
            form = ArticleForm(instance = article_obj)
        else:
            form = ArticleForm()
    context_variables = RequestContext(request) 
    return render_to_response('article_index.html', locals(), context_variables)






