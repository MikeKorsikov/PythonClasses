from django.contrib import admin
from django.urls import path, include
from sportapp import views

# added here all the required pages as per exercise
urlpatterns = [
    path('admin/', admin.site.urls), #  login admin, password admin
    path('', views.main, name='main'),
    path('football/', views.football, name='football'),
    path('hockey/', views.hockey, name='hockey'),
    path('basketball/', views.basketball, name='basketball'),
]

handler404 = 'sportapp.views.error_404_view'
