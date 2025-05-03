from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'created_at'
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    list_per_page = 20
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        # Allow superusers to delete
        if request.user.is_superuser:
            return True
        return False
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "پیام‌های انتخاب شده را به عنوان خوانده شده علامت بزن"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "پیام‌های انتخاب شده را به عنوان خوانده نشده علامت بزن"
    
    actions = ['mark_as_read', 'mark_as_unread']

admin.site.register(ContactMessage, ContactMessageAdmin)
