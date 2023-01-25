from django.contrib import admin
from django.urls import path, include
from account import views
from account.views import UserLoginView, UserRegistrationView
from imageUploader.views import ImageUploadView 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('home/',ImageUploadView.as_view(),name='home'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
