from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Job,Country,State,City
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

def viewcountry(request):
    cdata = Country.objects.all()
    return render(request,"practiceapp/viewcountry.html",{"ckey":cdata})
def viewstate(request):
    #sdata = State.objects.filter(country_id=request.GET["q"])
    country=Country.objects.get(pk=request.GET["q"])
    sdata = country.state_set.all()
    return render(request,"practiceapp/viewstate.html",{"skey":sdata})
def viewcity(request):
   # ctdata = City.objects.filter(city_id=request.GET["q"])
    state=State.objects.get(pk=request.GET["q"])
    ctdata = state.city_set.all()
    return render(request,"practiceapp/viewcity.html",{"ctkey":ctdata})