from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *


def forms(request):
    if request.method=='POST':
        username=request.POST['un']
        return HttpResponse('Data Submitted')

    return render(request,'form.html')


def schoolform(request):
    if request.method=='POST':
        sname=request.POST['sn']
        slocation=request.POST['sl']
        sprincipal=request.POST['sp']
        QOSC=create_school.objects.get_or_create(sname=sname,slocation=slocation,sprincipal=sprincipal)[0]
        QOSC.save()
        return HttpResponse('schol is created')

    return render(request,'schoolform.html')
