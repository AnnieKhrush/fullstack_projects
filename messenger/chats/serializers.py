from rest_framework import serializers
from chats.models import Chat, Message
from users.models import User

class ChatCreateSerializer(serializers.ModelSerializer):

    chat_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)


    class Meta:
        model = Chat
        fields = ('chat_title', 'chat_description', 'chat_users')


    def validate_data(self, data):
        if data['chat_title'] == '' or data['chat_description'] == '':
            raise serializers.ValidationError('Поле "название чата" или поле "описание чата" не должны быть пустыми!')
        return data
    

    def create(self, validated_data):
        chat_users = validated_data.pop('chat_users')
        instance = Chat.objects.create(**validated_data)
        instance.chat_users.add(*chat_users)
        return instance


class ChatChangeSerializer(serializers.ModelSerializer):

    chat_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)


    class Meta:
        model = Chat
        fields = ('chat_title', 'chat_description', 'chat_users')


    def validate(self, data):
        if data['chat_title'] == '' or data['chat_description'] == '':
            raise serializers.ValidationError('Поле "название чата" или поле "описание чата" не должны быть пустыми!')
        return data


class ChatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('chat_title', 'chat_description')


class MessageCreateSerializer(serializers.ModelSerializer):

    message_in_chat = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all())


    class Meta:
        model = Message
        fields = ('message', 'message_in_chat')
    

    def create(self, validated_data):
        instance = Message.objects.create(**validated_data)
        return instance


class MessageChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('message',)


class MessageCheckedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('checked',)

    
class MessageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('message', 'message_created_at', 'checked')
