from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, SearchListViews

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('posts/', PostsList.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdate.as_view(),name='post_update'),
    path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', SearchListViews.as_view(), name='post_search'),
]