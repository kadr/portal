from django.db import models


class Technology(models.Model):
    """Технологии"""

    title = models.CharField(max_length=255, default="",
                             verbose_name="Заголовок")
    created_at = models.DateTimeField(
        verbose_name="Добавлена", auto_now_add=True)

    class Meta:
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"

    def __str__(self):
        return self.title
