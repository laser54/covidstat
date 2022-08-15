from django.contrib import admin
from .models import Region

@admin.register(Region)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'region', 'sick', 'died')
    pass
