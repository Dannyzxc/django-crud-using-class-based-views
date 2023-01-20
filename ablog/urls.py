from .models import *
from .views import *
from django.urls import path
# from .import views


urlpatterns = [
    # path('', views.blog, name='blog'),
    path('', Blog.as_view(), name='my-blog'),
    path('article/<int:pk>', Article_Blog.as_view(), name='my-article'),
    path('addpost/', Add_post.as_view(), name='my-post'),
    path('article/edit/<int:pk>', update_post.as_view(), name='update-post'),
    path('article/delete/<int:pk>', destroy_post.as_view(), name='delete-post'),


]
 