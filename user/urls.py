from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.userLogIn, name='logIn'),
    path('logout/', views.logOut, name='logout'),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
]
