from django.contrib import admin 
from django.contrib.admin.models import LogEntry
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email','role')
    search_fields = ('last_name', 'first_name', 'email','role')

admin.site.register(User,UserAdmin)
admin.site.register(Session)
admin.site.register(Role)
admin.site.register(LogEntry)