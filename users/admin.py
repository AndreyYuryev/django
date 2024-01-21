from django.contrib import admin
from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'country', 'avatar',)
    list_filter = ('email', 'country',)
    search_fields = ('email', 'first_name', 'last_name',)
