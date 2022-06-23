from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class PostAdmin(admin.ModelAdmin):
    """Inquiry table on admin page"""
    list_filter = ('created_on',)
    list_display = ('email', 'user', 'created_on')
    search_fields = ('user__username', 'email')
