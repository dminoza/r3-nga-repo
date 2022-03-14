from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Post

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'post/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')[:4]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'post/detail.html'

