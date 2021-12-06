from django.contrib import admin
from .models import Task
from .models import Lecturer

admin.site.register(Task)

class LecturerAdmin(admin.ModelAdmin):
    list_display = ("instructor", "section","Title",)

admin.site.register(Lecturer,LecturerAdmin)