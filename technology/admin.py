from django.contrib import admin
from technology.models import Technology


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at"]
    list_display_links = ["id", "title"]
    readonly_fields = ["created_at"]


admin.site.register(Technology, TechnologyAdmin)
