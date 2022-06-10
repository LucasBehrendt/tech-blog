from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/create_post/', views.PostCreate.as_view(), name='create_post'),
    path('post/<int:pk>/update_post', views.PostUpdate.as_view(
        ), name='update_post'),
    path('post/<int:pk>/delete_post', views.PostDelete.as_view(
        ), name='delete_post'),
    path('post/<int:pk>/like', views.PostLike.as_view(), name="post_like"),
    path('blog/about/', views.About.as_view(), name='about'),
]
