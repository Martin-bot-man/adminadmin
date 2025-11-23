from django.urls import path
from .views import BookViewCreateAPIView

urlpatterns =[
    path('books/', BookViewCreateAPIView.as_view(), name = 'book-list-create')
]