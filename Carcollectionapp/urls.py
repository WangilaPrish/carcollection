
from django.contrib import admin
from django.urls import path, include
from Carcollectionapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('mustang/', views.mustang, name='mustang'),
    path('ferrari/', views.ferrari, name='ferrari'),
    path('chevrolet/', views.chevrolet, name='chevrolet'),
    path('porsche/', views.porsche, name='porsche'),
    path('camaro/', views.camaro, name='camaro'),
]
