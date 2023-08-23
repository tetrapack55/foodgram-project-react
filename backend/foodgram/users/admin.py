from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name',
                    'last_name', 'password')
    search_fields = ('username',)
    empty_value_display = '-пусто-'
