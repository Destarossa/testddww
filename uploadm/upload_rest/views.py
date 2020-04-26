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



class ManipulateView(APIView) :
	filex = MyImage.objects.order_by('-pk')[0]
	print(filex)
	image = filex.model_pic
	route = f'/media/{str(image)}'
	
	print( route )
	img = cv2.imread(route, 0) 
		# img = url_to_image(img_for_box_extraction_path)
	(thresh, img_bin) = cv2.threshold(img, 128, 255,
										cv2.THRESH_BINARY | cv2.THRESH_OTSU)  
	img_b = 255-img_bin
	print( img_b )


