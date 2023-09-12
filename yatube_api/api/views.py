from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsOwnerOrReadOnly
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)
from posts.models import Comment, Follow, Group, Post


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly)

    def get_post_object(self):
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        return Comment.objects.filter(post=self.get_post_object())

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post_object()
        )


class FollowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
