from django.shortcuts import render
from .models import MyModel
from .serializers import MyModelSerializer


class BookViewCreateAPIView(generics.ListCreateAPIView)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
