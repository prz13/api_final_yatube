from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

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


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    followed_user = serializers.ReadOnlyField(source='following.username')
    follower_user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Follow
        fields = ['id', 'followed_user', 'follower_user', 'created_at']

    def validate(self, data):
        followed_user = data.get('following')
        follower_user = self.context['request'].user

        if followed_user == follower_user:
            raise serializers.ValidationError(
                  'Вы не можете подписаться на самого себя.'
                                             )

        existing_follow = Follow.objects.filter(
           user=follower_user,
           following=followed_user
        ).exists()
        if existing_follow:
            raise serializers.ValidationError(
                'Вы уже подписаны на данного пользователя.'
                                             )

        return data

    def update(self, instance, validated_data):
        return instance
