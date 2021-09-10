from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include     
from .routers import router 

urlpatterns = [
    path('', include(router.urls)), 
]