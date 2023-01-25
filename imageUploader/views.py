from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer
from PIL import Image as Img
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from django.contrib import messages


class ImageUploadView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/home.html'
    style = {'template_pack': 'rest_framework/vertical/'} 

    def get(self, request):
        serializer = ImageSerializer()
        return Response({'serializer': serializer, 'style': self.style})
   
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.FILES)

        if serializer.is_valid():
            serializer.save()
            img = serializer.instance
            return Response({'serializer': serializer,'img':img ,'style': self.style })
        else:
            serializer = ImageSerializer()
            messages.success(request, 'please select a image')
            return redirect('home')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

