from .serializers import imageSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .models import *
from django.views.generic import View, DetailView 
import numpy as np
import cv2


class ImageCreateAPIView(generics.CreateAPIView):
	serializer_class = imageSerializer
	queryset = MyImage.objects.all()





