from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
]

handler404 = 'App.views.error_404_view'