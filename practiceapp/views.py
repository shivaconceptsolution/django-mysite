from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Job,Country,State,City
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.http import HttpResponse
def reg(request):
    if request.method=='POST':
        user = User.objects.create_user(request.POST['txtuser'],request.POST['txtemail'],request.POST['txtpass'])
        user.first_name=request.POST['txtfirst']
        user.last_name=request.POST['txtlast']
        user.save()
        return render(request,"practiceapp/reg.html",{"key":"data inserted successfully"})
    else:
        return render(request,"practiceapp/reg.html")
def loginuser(request):
    if request.method=='POST':
        obj = authenticate(username=request.POST['txtemail'],password=request.POST['txtpass'])
        if obj is not None:
            login(request,obj)
            return redirect('/practice/viewreg')
        else:
            return render(request,"practiceapp/login.html",{"key":"invalid emailid and password"})
    else:
        return render(request,"practiceapp/login.html")
def logoutuser(request):
    #del request.session['uid']
    logout(request)
    return redirect('/practice/loginuser')
def viewreg(request):
    if request.user.is_authenticated:
      obj = User.objects.all()
      return render(request,"practiceapp/viewreg.html",{"key":obj})
    else:
        return redirect('/practice/loginuser')

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
def ajaxload(request):
    return render(request,"practiceapp/search.html")
def ajaxdata(request):
    data = request.GET["q"]
    res=State.objects.filter(sname__contains=data)
    return render(request,"practiceapp/ajaxdata.html",{"key":res})
def displaycity(request):
    data=request.GET["q"]
    res = City.objects.filter(city_id=data)
    return render(request,"practiceapp/citydata.html",{"key":res})

def createcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('ckey', 'hello')
    return response
def getcookie(request):
    a  = request.COOKIES['ckey']
    return HttpResponse("value is "+  a);
