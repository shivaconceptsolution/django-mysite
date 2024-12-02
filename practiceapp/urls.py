from practiceapp.views import Addition,SI,JobCreate,JobList
from django.urls import path
from . import views

urlpatterns=[
    path('',Addition.as_view()),
    path('si',SI.as_view()),
    path('jobcreate',JobCreate.as_view()),
    path('joblist',JobList.as_view()),
    path('viewcountry',views.viewcountry,name='viewcountry'),
    path('viewstate',views.viewstate,name='viewstate'),
    path('viewcity',views.viewcity,name='viewcity')

]