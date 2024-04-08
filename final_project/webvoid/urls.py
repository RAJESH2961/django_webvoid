from django.urls import path
from webvoid import views
from .views import iframe
urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('iframe/',iframe,name="iframe"),

    path('contact/', views.contact, name='contact'),
    path('success/', views.successpage, name='success_page'),
    
]
