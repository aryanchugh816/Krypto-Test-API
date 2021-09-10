from rest_framework import routers
from .viewsets import EventViewSet

router = routers.DefaultRouter()
router.register(r'', EventViewSet, basename='event')