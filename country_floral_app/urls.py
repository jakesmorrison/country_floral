from django.conf.urls import url

from . import views

app_name = 'country_floral_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'get_distance', views.get_distance, name='get_distance'),
    url(r'order/', views.order, name='order'),
    url(r'process/', views.process, name='process'),
    url(r'about/', views.about, name='about'),
    url(r'contact/', views.contact, name='contact'),
    url(r'gallery/',views.gallery, name='gallery'),
    url(r'events/', views.events, name='events'),
]