from django.urls import path
from myapp import views

urlpatterns = [
 path('', views.index, name='my_index'),
 path('about/', views.about, name='my_about'),
 path('contact/', views.contact, name='my_contact'),
 path('home/', views.home, name='my_home'),
 path('gallery/', views.gallery, name='my_gallery')]

