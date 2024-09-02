from django.contrib import admin
from .models import Category, Priority, Task

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
    list_filter = ('status',)

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)
    list_filter = ('status',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'date_start', 'date_end', 'participants')
    search_fields = ('title', 'description')
    list_filter = ('category', 'priority', 'participants', 'date_start', 'date_end')
    autocomplete_fields = ['participants']

# Registering the models manually (alternative to using @admin.register)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Priority, PriorityAdmin)
# admin.site.register(Task, TaskAdmin)
