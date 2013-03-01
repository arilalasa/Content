
from django.forms import ModelForm,Textarea
from articles.models import Article
from django.shortcuts import render_to_response
from django import forms
from datetime import datetime

class ArticleForm(ModelForm):
   # title=MyFormField(help_text="Title iof the page")
     class Meta:
        model=Article
        exclude=('created_at','modified_at')
        widgets={
                'content':Textarea(attrs={'cols':100,'rows':20}),
                
                }
        
