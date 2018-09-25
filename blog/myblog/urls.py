
from django.conf.urls import url

from myblog import views

urlpatterns =[
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^info/', views.info, name='info')
]