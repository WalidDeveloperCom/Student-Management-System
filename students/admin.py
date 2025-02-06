from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'course')
    list_filter = ('course',)
    search_fields = ('name', 'email', 'course')
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'email')
        }),
        ('Additional Information', {
            'fields': ('phone_number', 'course')
        }),
    )

