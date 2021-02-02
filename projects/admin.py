from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'type_con',
                    'price', 'list_date', 'certificate')
    list_display_links = ('id', 'title')
    list_filter = ('certificate',)
    list_editable = ('is_completed',)
    search_fields = ('title', 'description', 'type_con', 'city', 'state', 'price')
    list_per_page = 25


admin.site.register(Project, ProjectAdmin)
