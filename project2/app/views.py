from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def insert_country(request):
    ECMFO=CountryModelForm()
    d={'ECMFO':ECMFO}
    if request.method=='POST':
        CMFO=CountryModelForm(request.POST)
        if CMFO.is_valid():
            CMFO.save()
            return HttpResponse('Country is created')
        else:
            return HttpResponse('Invalid data')

    return render(request,'insert_country.html',d)

def insert_capital(request):
    ECAMFO=CapitalModelForm()
    d={'ECAMFO':ECAMFO}
    if request.method=='POST':
        CAMFO=CapitalModelForm(request.POST)
        if CAMFO.is_valid():
            CAMFO.save()
            return HttpResponse('Capital is created')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_capital.html',d)



