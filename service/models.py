from django.db import models
from colorfield.fields import ColorField


class Service(models.Model):
    """Услуги"""

    title = models.CharField(max_length=255, default="",
                             verbose_name="Заголовок")
    color = ColorField(default='#FF0000')
    created_at = models.DateTimeField(
        verbose_name="Добавлена", auto_now_add=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title
