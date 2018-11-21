from django.contrib import admin
from service.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at"]
    list_display_links = ["id", "title"]
    readonly_fields = ["created_at"]


admin.site.register(Service, ServiceAdmin)
