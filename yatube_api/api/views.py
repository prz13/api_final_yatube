from django.shortcuts import get_object_or_404
from posts.models import Group, Post, Comment
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, filters, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, 
                         GroupSerializer,
                         PostSerializer, 
                         FollowSerializer)

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        post = self.get_post()
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

class FollowViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.following

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
