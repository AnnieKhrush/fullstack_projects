from django.contrib import admin

# Register your models here.
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'user_chats')
    search_fields = ('username',)

admin.site.register(User)