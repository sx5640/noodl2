from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def source_detail(request, source_name):
    return HttpResponse('source: ' + source_name)

def article_detail(request, source_name, article_id):
    return HttpResponse('source: ' + source_name + ', article ' + article_id)


