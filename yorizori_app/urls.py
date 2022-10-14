from django.urls import path
from yorizori_app import views 


urlpatterns = [
    path('', views.index),
    path('addSource/', views.addSource)

]
