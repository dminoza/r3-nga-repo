from django.urls import path, include

urlpatterns =[
    path('post/', include('posts.urls'), name='index'),
    path('accounts/', include('allauth.urls'))
]