from rest_framework import viewsets
from .serializers import TodoItemSerializer
from .models import TodoItem


class TodoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
