from django.contrib import admin

from list_app.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'description', 'status', 'deadline_date', 'created_at')
    list_filter = ('id', 'status', 'deadline_date', 'created_at')
    search_field = ('status', 'deadline_date')
    fields = ('task', 'status','description', 'deadline_date', 'created_at')


admin.site.register(Task, TaskAdmin)