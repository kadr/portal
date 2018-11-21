from datetime import datetime

from django.db import models
from django.utils.html import format_html
from service.models import Service
from sphere.models import Sphere
from technology.models import Technology
from ckeditor_uploader.fields import RichTextUploadingField


class Case(models.Model):
    """Кейсы"""

    title = models.CharField(max_length=255, default="",
                             verbose_name="Заголовок")
    link = models.CharField(max_length=255, default="",
                            verbose_name="Ссылка на кейс")
    product_link = models.CharField(max_length=255, default="",
                                    verbose_name="Ссылка на продукт")
    description = RichTextUploadingField(verbose_name="Описание", default="")
    logo = models.ImageField(upload_to="cases/%Y/%m/%d/",
                             verbose_name="Лого")
    preview_picture = models.ImageField(upload_to="cases/%Y/%m/%d/",
                                        verbose_name="Превьешка")
    services = models.ManyToManyField(
        Service,
        related_name="cases",
        verbose_name="Услуги")
    spheres = models.ManyToManyField(
        Sphere,
        related_name="cases",
        verbose_name="Отрасли")
    technologies = models.ManyToManyField(
        Technology,
        related_name="cases",
        verbose_name="Технологии")
    date_start = models.DateTimeField(
        verbose_name="Дата старта", default=datetime.now())
    date_end = models.DateTimeField(
        verbose_name="Дата окончания", default=datetime.now())

    class Meta:
        ordering = ["-date_start"]
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"

    def __str__(self):
        return self.title

    def logo_tag(self):
        """тег для поля logo"""
        if self.logo:
            return format_html("<img src='/static/media/{}' \
            width='400'/>".format(self.logo))
        else:
            return format_html("<img src='/static/images/blank.png' \
            width='200'/>")

    def preview_picture_tag(self):
        """тег для поля preview_picture"""
        if self.preview_picture:
            return format_html("<img src='/static/media/{}' \
            width='400'/>".format(self.preview_picture))
        else:
            return format_html("<img src='/static/images/blank.png' \
            width='200'/>")

    def logo_thumbnail(self):
        """тег для поля preview_picture"""
        if self.logo:
            return format_html("<img src='/static/media/{}' \
            width='100'/>".format(self.logo))
        else:
            return format_html("<img src='/static/images/blank.png' \
            width='50'/>")

    logo_tag.short_description = "Изображение"
    preview_picture_tag.short_description = "Изображение"
    logo_thumbnail.short_description = "Логотип"


class File(models.Model):
    """Файлы для кейсов"""

    file = models.FileField(upload_to="cases/%Y/%m/%d/",
                            verbose_name="Файл")
    created_at = models.DateTimeField(
        verbose_name="Добавлена", auto_now_add=True)
    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        related_name="files",
        )

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

    def __str__(self, arg):
        return self.file
