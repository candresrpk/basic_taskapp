
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signupView, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('tasks/', include('applications.taski.urls')),
]
