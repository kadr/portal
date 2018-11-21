from django.db import models


class Sphere(models.Model):
    """Услуги"""

    title = models.CharField(max_length=255, default="",
                             verbose_name="Заголовок")
    created_at = models.DateTimeField(
        verbose_name="Добавлена", auto_now_add=True)

    class Meta:
        verbose_name = "Отрасль"
        verbose_name_plural = "Отрасли"

    def __str__(self):
        return self.title
