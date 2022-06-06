from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/create_post/', views.PostCreate.as_view(), name='create_post'),
    path('blog/about/', views.About.as_view(), name='about'),
]
