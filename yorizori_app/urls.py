from django.urls import path
from yorizori_app import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('addSource/', views.addSource),
    path('login/', views.login),
    path('singUp/', views.singUp),
    path('search/', views.search, name='search'),
    path('home2/', views.home2),
    path('upload/', views.Upload),
    path('edit/<int:recipe_id>/',views.Edit, name='edit'),
    path('delete/<int:recipe_id>/', views.Delete, name='delete'),
    path('MyRecipe/', views.MyRecipe),
    path('contents/<int:recipe_id>/', views.contents),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

