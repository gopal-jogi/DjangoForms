from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.
def topic(request):
    ETFO=TopicForms()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TTDO=TopicForms(request.POST)
        if TTDO.is_valid():
            tn=TTDO.cleaned_data['TName']
            TO=Topic.objects.get_or_create(TName=tn)[0]
            TO.save()
            return HttpResponse("Topic is created Succesfully")
        else:
            return HttpResponse("Data is invalided")
    return render(request,'topic.html',d)

def webpage(request):
    EWFO=WebPageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WEDO=WebPageForm(request.POST)
        if WEDO.is_valid():
            tn=WEDO.cleaned_data['TName']
            TO=Topic.objects.get(TName=tn)
            n=WEDO.cleaned_data['Name']
            u=WEDO.cleaned_data['URL']
            e=WEDO.cleaned_data['Email']
            WO=WebPage.objects.get_or_create(TName=TO,Name=n,URL=u,Email=e)[0]
            WO.save()
            return HttpResponse("Webpage Create Successfully")
        else:
            return HttpResponse("INvalide Data")
    return render(request,'webpage.html',d)

def accessrecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        ADO=AccessRecordForm(request.POST)
        if ADO.is_valid():
            n=ADO.cleaned_data['Name']
            WO=WebPage.objects.get(Name=n)
            d=ADO.cleaned_data['Date']
            a=ADO.cleaned_data['Author']
            AO=AccessRecord.objects.get_or_create(Name=WO,Date=d,Author=a)[0]
            AO.save()
            return HttpResponse("Access Record is created")
        else:
            return HttpResponse("Invalide data")


    return render(request,'accessrecord.html',d)

