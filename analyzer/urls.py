from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('/hello2', views.hello2),
    path('/trivy', views.trivy)
]
