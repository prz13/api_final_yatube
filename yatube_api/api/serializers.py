from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        fields = '__all__'
        model = Follow

    def validate(self, data):
        following = data.get('following')
        user = self.context['request'].user

        if user == following:
            raise serializers.ValidationError(
                  'Вы не можете подписаться на самого себя.')

        existing_follow = Follow.objects.filter(
            user=user,
            following=following).exists()

        if existing_follow:
            raise serializers.ValidationError(
                'Вы уже подписаны на данного пользователя.')

        return data
