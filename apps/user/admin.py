from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ('User Credentials', {
            'fields': ('email', 'username', 'password', 'first_name', 'last_name', 'phone_number',)
        }),

        ('Basic', {
            'fields': ('unique_code', 'date_of_birth',
                       'user_image', 'type', 'is_staff', 'is_active', 'branch', 'organization',
                       'last_login', 'date_joined', 'created_by', 'modified_by', 'modified_datetime', 'status',)
        }),
    )
    readonly_fields = ['date_joined']


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserPermissions)
# admin.site.register(ThirdPartyIntegration)
