from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))
    thumbnail.short_description='Img'
    list_display=('id','thumbnail','f_name','designation','created_date')
    list_diaplay_links=('id','thumbnail','f_name',)
    search_fields=('f_name','designation')
    list_filter=('designation',)
admin.site.register(Team,TeamAdmin)
