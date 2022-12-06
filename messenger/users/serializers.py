from rest_framework import serializers
from users.models import User
from chats.models import Chat
from users.tasks import send_admin_email


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
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        user_chats = validated_data['user_chats']
        chats_id = []
        for chat in user_chats:
            if chat.admins.filter(id=user.id).exists():
                if chat.chat_users.filter(id=instance.id).exists():
                    raise serializers.ValidationError('Пользователь уже в этом чате!')
                else:
                    instance.user_chats.add(chat)
                    instance.save()
                    chats_id.append(chat.id)
                    
            else:
                raise serializers.ValidationError('Пользователь не является админом чата, поэтому не может добавлять других пользователей в этот чат!')
        
        send_admin_email.delay(instance.id, chats_id)
        return instance


class UserDeleteSerializer(serializers.ModelSerializer):

    user_chats = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all(), many=True)


    class Meta:
        model = User
        fields = ('user_chats',)



    def update(self, instance, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        user_chats = validated_data['user_chats']
        for chat in user_chats:
            if chat.admins.filter(id=user.id).exists():
                if chat.chat_users.filter(id=user.id).exists():
                    instance.user_chats.remove(chat)
                    instance.save()
                else:
                    raise serializers.ValidationError('Пользователя нет в этом чате!')
            else:
                raise serializers.ValidationError('Пользователь не является админом чата, поэтому не может удалять других пользователей из этого чата!')

        instance.save()
        return instance
