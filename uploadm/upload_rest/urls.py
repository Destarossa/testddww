from django.conf.urls import include, url
from .views import ImageCreateAPIView, ManipulateView

urlpatterns = [
    url(r'^upload/$', ImageCreateAPIView.as_view()),
    url(r'^show/$', ManipulateView.as_view()),

]
