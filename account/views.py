from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserLoginSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import messages

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [TemplateHTMLRenderer]
  template_name = 'app/register.html'
  style = {'template_pack': 'rest_framework/vertical/'}  
  
  def get(self, request, format=None):
    serializer = UserRegistrationSerializer()
    return Response({'serializer': serializer, 'style': self.style})

  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    
    serializer.is_valid(raise_exception=True)
    messages.success(request, 'registerd successfully')
    user = serializer.save()

    return Response({'serializer': serializer, 'style': self.style})

class UserLoginView(APIView):
  renderer_classes = [TemplateHTMLRenderer]
  template_name = 'app/login.html'
  style = {'template_pack': 'rest_framework/vertical/'}  

  def get(self, request, format=None):
    serializer = UserLoginSerializer()
    return Response({'serializer': serializer, 'style': self.style})

  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      return Response({'serializer': serializer, 'style': self.style})
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}})

def home(request):
 return render(request, 'app/home.html')
 