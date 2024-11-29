from practiceapp.views import Addition,SI,JobCreate,JobList
from django.urls import path

urlpatterns=[
    path('',Addition.as_view()),
    path('si',SI.as_view()),
    path('jobcreate',JobCreate.as_view()),
    path('joblist',JobList.as_view())
]