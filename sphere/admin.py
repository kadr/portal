from django.contrib import admin
from sphere.models import Sphere


class SphereAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at"]
    list_display_links = ["id", "title"]
    readonly_fields = ["created_at"]


admin.site.register(Sphere, SphereAdmin)
