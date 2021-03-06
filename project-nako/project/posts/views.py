from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer

# Create your views here.

# class IndexView(generic.ListView):
#     template_name = 'post/index.html'
#     context_object_name = 'post_list'

#     def get_queryset(self):
#         return Post.objects.order_by('-created_at')[:4]


# class DetailView(generic.DetailView):
#     model = Post
#     template_name = 'post/detail.html'


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = [IsAuthenticated]


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


