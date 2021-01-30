from django.contrib import admin

from .models import Certificate

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_mvp', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    list_editable = ('is_mvp',)

admin.site.register(Certificate, CertificateAdmin)