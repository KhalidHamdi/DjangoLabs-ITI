# tracking_system/urls.py
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('tracking/',views.tracking,name="tracking")

]
