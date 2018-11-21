from django.contrib import admin
from case.models import Case, File
from service.models import Service
from jet.admin import CompactInline
from django.utils.html import format_html
from django.db.models.fields import IntegerField, AutoField


class ServicesListFilter(admin.SimpleListFilter):
    """
    переопределяем фильтр для услуг
    """

    title = "Услуги"
    parameter_name = "services__id__in"
    template = "admin/custom_filter.html"

    def lookups(self, request, model_admin):
        """
        возвращаем все услуги для тега селект
        """

        services = Service.objects.all()
        for service in services:
            yield (str(service.id), service.title)

    def expected_parameters(self):
        return [self.lookup.kwarg]

    def values(self):
        """
        Returns a list of values to filter on.
        """
        values = []
        value = self.used_parameters.get(self.lookup_kwarg, None)
        if value:
            values = value.split(",")
        # convert to integers if IntegerField
        if type(self.field.rel.to._meta.pk) in [IntegerField, AutoField]:
            values = [int(x) for x in values]

        return values

    def queryset(self, request, queryset):
        """
        выполняем фильтрацию типа WHERE IN ()
        """
        if self.value():
            return queryset.filter(services__in=self.value().split(","))
        return queryset

    def choices(self, cl):
        services = Service.objects.all()
        for service in services:
            print(cl.get_query_string({}, [self.parameter_name]))
            yield {
                "selected": self.value() is None,
                "query_string": "",
                "display": service.title
            }


class FileInline(CompactInline):
    model = File
    extra = 5


class CaseAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Основные параметры", {"fields": [
         "date_start", "date_end", "title", "link", "product_link"]}),
        ("Описание", {"fields": ["description"]}),
        ("Изображения", {"fields": [("logo_tag", "logo"),
                                    ("preview_picture_tag",
                                     "preview_picture")]}),
        ("Категории", {"fields": ["services", "spheres", "technologies"]}),
    ]
    list_select_related = True
    list_display = ["id", "title", "link", "serviceList",
                    "logo_thumbnail",
                    "date_start", "date_end"]
    list_display_links = ["id", "title"]
    list_filter = ["date_start", "date_end", ServicesListFilter,
                   "spheres", "technologies"]
    readonly_fields = ["logo_tag", "preview_picture_tag"]
    list_per_page = 10

    inlines = [
        FileInline
    ]

    def serviceList(self, obj):
        """рисуем цветные кружки"""
        services = ""
        for item in obj.services.values("title", "color"):
            services += "<div style='background-color:{}; \
            border-radius: 50px; width: 16px; margin-bottom: 10px;\
            margin-right: 5px; float:left'>&nbsp;</div>{}<br /><br />" \
            .format(item.get("color"), item.get("title"))

        return format_html(services)

    serviceList.short_description = "Услуги"


admin.site.register(Case, CaseAdmin)
