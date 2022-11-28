from rest_framework import serializers
from users.models import User
from chats.models import Chat


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'date_of_birth', 'place_of_living', 'user_info')


class UserAddSerializer(serializers.ModelSerializer):

    user_chats = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all(), many=True)


    class Meta:
        model = User
        fields = ('user_chats',)


    def update(self, instance, validated_data):
        user_chats = validated_data.pop('user_chats')
        for chat in user_chats:
            if chat.chat_users.filter(id=instance.id).exists():
                raise serializers.ValidationError('Пользователь уже в этом чате!')
            else:
                instance.user_chats.add(chat)
        return instance


class UserDeleteSerializer(serializers.ModelSerializer):

    user_chats = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all(), many=True)


    class Meta:
        model = User
        fields = ('user_chats',)


    def update(self, instance, validated_data):
        user_chats = validated_data.pop('user_chats')
        for chat in user_chats:
            if chat.chat_users.filter(id=instance.id).exists():
                instance.user_chats.remove(chat)
            else:
                raise serializers.ValidationError('Пользователя нет в этом чате!')
        return instance
