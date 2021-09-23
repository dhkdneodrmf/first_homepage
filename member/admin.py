from django.contrib import admin
from .models import User
# Register your models here.

class Userconfig(admin.ModelAdmin):
    readonly_fields=('registered',)

admin.site.register(User,Userconfig)