from django.http import HttpResponse
from django.shortcuts import render
from .models import Information,Education,Work_Experience,Skills,Contact


def index(request):
    info=Information.objects.all()
    edu=Education.objects.all()
    work_exp=Work_Experience.objects.all()
    skill=Skills.objects.all()
    
    if request.method== 'POST':
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        phone=request.POST.get('phone')
        Message=request.POST.get('Message')
        c=Contact(Name=Name, Email=Email, phone=phone, Message=Message)
        c.save()
        return render(request,'Resume/index.html',{'info': info,'edu':edu, 'work_exp':work_exp,'skill':skill})
    else:
        return render(request,'Resume/index.html',{'info': info,'edu':edu, 'work_exp':work_exp,'skill':skill})
    return render(request,'Resume/index.html',{'info': info,'edu':edu, 'work_exp':work_exp,'skill':skill})
