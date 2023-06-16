from app1.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('sample1/',sample1,name='sample1'),
    path('sample/',sample,name='sample')
]