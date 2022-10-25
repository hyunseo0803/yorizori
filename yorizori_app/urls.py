from django.urls import path
from yorizori_app import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('addSource/', views.addSource),
    path('login/', views.login),
    path('singUp/', views.singUp),
    path('search/', views.search),
    # path('success/', views.success),
]


