from django.urls import path

from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns =[
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('', PostListCreateAPIView.as_view(), name='post-index'),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name="post-update-retrieve-destroy")
]