from django.contrib import admin
from applications.taski.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

admin.site.register(Task, TaskAdmin)