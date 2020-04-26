from django.conf.urls import include, url
from .views import ImageCreateAPIView

urlpatterns = [
    url(r'^upload/$', ImageCreateAPIView.as_view()),
    

]
