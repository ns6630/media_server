from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=100, blank=True, unique=True)
    img = models.ImageField(upload_to="media/img/")
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class ResponseSettings(models.Model):
    class Mode(models.TextChoices):
        NORMAL = 'normal', 'Normal'
        ERROR = 'error', 'Error'

    mode = models.CharField(
        max_length=6,
        choices=Mode,
        default=Mode.NORMAL
    )
