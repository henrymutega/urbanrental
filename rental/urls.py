from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^property/', views.property, name='property'),
    url(r'^propertysingle/(\d+)',views.propertysingle,name ='propertysingle'),
    url(r'^blog/', views.blog , name='blog'),
    url(r'^blogsingle/(\d+)',views.blogsingle,name ='blogsingle'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),
    url(r'^service/', views.service, name='service'),
]
