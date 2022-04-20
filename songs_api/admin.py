from django.contrib import admin

# Register your models here.
from .models import Song

class SongAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
    
admin.site.register(Song, SongAdmin)