from django.contrib import admin
from django.urls import path, include
from account import views
from account.views import UserLoginView, UserRegistrationView, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('home/',views.home,name='home'),
    
]
