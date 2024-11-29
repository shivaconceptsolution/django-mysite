from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Job
class Addition(View):
    def get(self,request):
        return render(request,"practiceapp/add.html")
    def post(self,request):
        a=request.POST.get("txtnum1")
        b=request.POST.get("txtnum2")
        c=int(a)+int(b)
        return render(request,"practiceapp/add.html",{"key":c})
class SI(View):
    def get(self,request):
        return render(request,"practiceapp/si.html")
    def post(self,request):
        a=request.POST.get("txtnum1")
        b=request.POST.get("txtnum2")
        c=request.POST.get("txtnum3")
        d=(float(a)*float(b)*float(c))/100
        return render(request,"practiceapp/si.html",{"key":d})
class JobCreate(CreateView):
    model = Job
    fields = ['jobtitle', 'jobdescription']
    success_url='/practice/si'
class JobList(ListView):
    model = Job   # Job.objects.all()   