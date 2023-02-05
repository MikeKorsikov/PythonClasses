from django.contrib import admin
from django.urls import path
from hornsandhooves import views

# added here all of the required pages as per exercise
urlpatterns = [
    path('admin/', admin.site.urls), #  login admin, password admin
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('management/', views.management, name='management'),
    path('news/', views.news, name='news'),
]
