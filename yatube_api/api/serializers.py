from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',)
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок на пользователей."""

    user = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), required=True, slug_field='username'
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following',),
                message='Подписка уже оформлена!'
            )
        ]

    def validate_following(self, following):
        """Валидация для ограничения подписки на самого себя."""
        if following == self.context['request'].user:
            raise serializers.ValidationError('Нельзя подписаться '
                                              'на самого себя!')
        return following


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп."""

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для публикаций."""

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post
