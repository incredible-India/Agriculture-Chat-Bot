from django.contrib import admin

# Register your models here.
#importing the db registration
from .models import User, ChatHistory

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')

class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'response', 'timestamp')

admin.site.register(User, UserAdmin)
admin.site.register(ChatHistory, ChatHistoryAdmin)