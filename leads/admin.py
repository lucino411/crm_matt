from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Lead, Agent, UserProfile, Category

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {
         'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions', 'is_organisor', 'is_agent')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        # ... Agrega tus propios fieldsets si es necesario ...
    )


class LeadAdmin(admin.ModelAdmin):
    # fields = (
    #     'first_name',
    #     'last_name',
    # )

    list_display = ['first_name', 'last_name', 'age', 'email']
    list_display_links = ['first_name']
    list_editable = ['last_name']
    list_filter = ['category']
    search_fields = ['first_name', 'last_name', 'email']


admin.site.register(Category)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Agent)





