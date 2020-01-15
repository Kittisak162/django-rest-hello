from django.conf.urls import url, include
from hello import views

urlpatterns = [
  url(r'^hello', views.Hello.as_view())
]