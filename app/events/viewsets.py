from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import HttpRequest

from .models import Events
from .permissions import IsOwner
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Events.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user.id)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)