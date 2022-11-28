from rest_framework import serializers
from chats.models import Chat, Message
from users.models import User

class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('chat_title', 'chat_description')


class ChatCreateSerializer(serializers.ModelSerializer):

    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Chat
        fields = ('chat_title', 'chat_description', 'users')
    
    def create(self, validated_data):
        users = validated_data.pop('users')
        instance = Chat.objects.create(**validated_data)
        instance.chat_users.add(users)
        return instance


class MessageCreateSerializer(serializers.ModelSerializer):

    chat_id = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all())

    class Meta:
        model = Message
        fields = ('message', 'chat_id')
    
    def create(self, validated_data):
        chat_id = validated_data.pop('chat_id')
        instance = Message.objects.create(**validated_data)
        instance.message_in_chat.add(chat_id)
        return instance


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('message', 'message_in_chat')

class MessageCheckedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('checked',)
