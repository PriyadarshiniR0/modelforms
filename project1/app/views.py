from django.shortcuts import render

from app.models import *
from app.forms import *

from django.http import HttpResponse
# Create your views here.

def insert_topic_mf(request):
    ETMFO=TopicModelForm()
    d={'ETMFO':ETMFO}
    if request.method=='POST':
        TDMFO=TopicModelForm(request.POST)
        if TDMFO.is_valid():
            TDMFO.save()
            return HttpResponse('Topic is created')
        else:
            return HttpResponse('Invalid data')
        
    return render(request,'insert_topic_mf.html',d)


def insert_webpage_mf(request):
    EWMFO=WebpageModelForm()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        WDMFO=WebpageModelForm(request.POST)
        if WDMFO.is_valid():
            WDMFO.save()
            return HttpResponse('Webpage is created')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_webpage_mf.html',d)

def insert_access_mf(request):
    EAMFO=AccessModelForm()
    d={'EAMFO':EAMFO}
    if request.method=="POST":
        ADMFO=AccessModelForm(request.POST)
        if ADMFO.is_valid():
            ADMFO.save()
            return HttpResponse('Access Record is created')
        else:
            return HttpResponse('Invalid data')
    
    return render(request,'insert_access_mf.html',d)
