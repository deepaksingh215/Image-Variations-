from django.contrib import admin
from django.urls import path, include
from account.views import UserLoginView, UserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    
]
