from rest_framework import serializers
from chats.models import Chat, Message
from users.models import User
from django.shortcuts import get_object_or_404

class MessageCreateSerializer(serializers.ModelSerializer):

    message_in_chat = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all())


    class Meta:
        model = Message
        fields = ('message', 'message_in_chat', 'owner')
    

    def create(self, validated_data):
        instance = Message.objects.create(**validated_data)
        return instance


class MessageChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('message', 'checked', 'owner', 'message_created_at')

    def update(self, instance, validated_data):
        instance.message = validated_data.get('message', instance.message)
        instance.checked = validated_data.get('checked', instance.checked)
        instance.save()
        return instance
    
 
class MessageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'message', 'message_created_at', 'checked', 'owner')


class ChatCreateSerializer(serializers.ModelSerializer):

    chat_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)


    class Meta:
        model = Chat
        fields = ('chat_title', 'chat_description', 'chat_users')


    def validate(self, data):
        if data['chat_title'] == '' or data['chat_description'] == '':
            raise serializers.ValidationError('Поле "название чата" или поле "описание чата" не должны быть пустыми!')
        return data
    

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        chat_users = validated_data.pop('chat_users')
        instance = Chat.objects.create(**validated_data)
        instance.chat_users.add(*chat_users)
        instance.admins.add(user)
        return instance


class ChatChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('chat_title', 'chat_description')


    def validate(self, data):
        if data['chat_title'] == '' or data['chat_description'] == '':
            raise serializers.ValidationError('Поле "название чата" или поле "описание чата" не должны быть пустыми!')
        return data


    def update(self, instance, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        if instance.admins.filter(id=user.id).exists():
            instance.chat_title = validated_data.get('chat_title', instance.chat_title)
            instance.chat_description = validated_data.get('chat_description', instance.chat_description)
            instance.save()
            instance.last_message = Message.objects.filter(message_in_chat=instance).latest('message_created_at')
        else:
            raise serializers.ValidationError('Пользователь не является админом чата, поэтому не может редактировать этот чат!')
        return instance


class ChatListSerializer(serializers.ModelSerializer):
    last_message = MessageListSerializer(source='get_message')


    class Meta:
        model = Chat
        fields = ('id', 'chat_title', 'chat_description', 'chat_messages', 'last_message')

