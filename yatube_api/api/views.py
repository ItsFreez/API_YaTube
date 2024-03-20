from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsOwnerOrReadOnly
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)
from posts.models import Group, Post


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Вьюсет миксин для методов GET (список всех объектов) и POST."""

    pass


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly)

    def get_post_object(self):
        """Получает объект публикации по id."""
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        """Получает список всех комментариев к указанной публикации."""
        return self.get_post_object().comments.all()

    def perform_create(self, serializer):
        """Метод создания объекта. Сохраняет автором текущего пользователя."""
        serializer.save(
            author=self.request.user,
            post=self.get_post_object()
        )


class FollowViewSet(CreateListViewSet):
    """Вьюсет для подписок на пользователей."""

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Получает список всех подписок текущего пользователя."""
        return self.request.user.subscriptions.all()

    def perform_create(self, serializer):
        """
        Метод создания объекта подписки.
        Указывает текущего пользователя, как автора подписки.
        """
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для публикаций."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """
        Метод создания объекта публикации.
        Указывает текущего пользователя, как автора подписки.
        """
        serializer.save(author=self.request.user)
