from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def database(request):
    s=Topic.objects.all()

    d={'s':s}
    return render(request,'database.html',d)
def database1(request):
    s=Webpage.objects.all()
    s=Webpage.objects.filter(topic_name='cricket')
    s=Webpage.objects.exclude(topic_name='cricket')
    s=Webpage.objects.all()[2::5]
    s=Webpage.objects.all().order_by('name')
    s=Webpage.objects.filter(topic_name='cricket').order_by('-name')
    s=Webpage.objects.all().order_by(Length('name'))
    s=Webpage.objects.all().order_by(Length('name').desc())
    d={'s':s}
    return render(request,'database1.html',d)
def database2(request):
    s=AccessRecords.objects.all()
    d={'s':s}
    return render(request,'database2.html',d)



    
