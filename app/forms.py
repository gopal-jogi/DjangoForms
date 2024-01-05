from django import forms
from app.models import *

class TopicForms(forms.Form):
    TName=forms.CharField()

class WebPageForm(forms.Form):
    TL=[[to.TName,to.TName] for to in Topic.objects.all() ]
    TName=forms.ChoiceField(choices=TL)
    Name=forms.CharField()
    URL=forms.URLField()
    Email=forms.EmailField()

class AccessRecordForm(forms.Form):
    WL=[[wo.Name, wo.Name] for wo in WebPage.objects.all()]
    Name=forms.ChoiceField(choices=WL)
    Date=forms.DateField()
    Author=forms.CharField()