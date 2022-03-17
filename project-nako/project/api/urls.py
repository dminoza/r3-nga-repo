from django.urls import path, include

urlpatterns =[
    path('post/', include('posts.urls'), name='index'),
    path('accounts/', include('rest_auth.urls')),
    path('accounts/registration/', include('rest_auth.registration.urls'))
]