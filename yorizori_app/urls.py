from django.urls import path
from yorizori_app import views 


urlpatterns = [
    path('', views.index),
    path('login.html/',views.login),
    path('logout/',views.logout),
    path('singup.html/', views.singup),
    path('Mupdate/', views.Mupdate)

]
