from django.shortcuts import render
from rest_framework import generics
# Create your views here.

from .models import Blog, FM
from .serializers import BlogSerializer


class ListBlog(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class DetailBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ListFM(generics.ListCreateAPIView):
    queryset = FM.objects.all()
    serializer_class = FMSerializer


class DetailFM(generics.RetrieveUpdateDestroyAPIView):
    queryset = FM.objects.all()
    serializer_class = FMSerializer
