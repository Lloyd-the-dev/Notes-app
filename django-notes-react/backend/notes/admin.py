from django.contrib import admin
from .models import Note

class Noteadmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'timestamp')


admin.site.register(Note, Noteadmin)
