from django.contrib import admin

# Register your models here.
from .models import Lyrics

class LyricsAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
admin.site.register(Lyrics, LyricsAdmin)