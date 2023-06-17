from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

# Регистрация представлений связанных с моделью Post
post_router = DefaultRouter()
post_router.register('', PostViewSet, basename='post')

# Регистрация представлений связанных с моделью Comment
comment_router = DefaultRouter()
comment_router.register('', CommentViewSet, basename='comment')

# Регистрация представления для модели Group
group_router = DefaultRouter()
group_router.register('', GroupViewSet, basename='group')

# Регистрация представления для модели Follow
follow_router = DefaultRouter()
follow_router.register('', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/posts/', include(post_router.urls)),
    path('v1/groups/', include(group_router.urls)),
    path('v1/posts/<int:post_id>/comments/', include(comment_router.urls)),
    path('v1/follow/', include(follow_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token, name='url_api_token'),
    path('v1/', include('djoser.urls.jwt')),
]
