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
    path('viewcity',views.viewcity,name='viewcity'),
    path('ajaxload',views.ajaxload,name='ajaxload'),
    path('ajaxdata',views.ajaxdata,name='ajaxdata'),
    path('displaycity',views.displaycity,name='displaycity'),
    path('reg', views.reg, name='reg'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('viewreg', views.viewreg, name='viewreg'),
    path('createcookie',views.createcookie,name='createcookie'),
    path('getcookie',views.getcookie,name='getcookie')

]