from io import BytesIO
import barcode
from barcode.writer import ImageWriter
from django.core.files import File
from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        EAN = barcode.codex.Code128
        ean = EAN(f'{self.name}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        buffer.seek(0)
        self.barcode.save(f'{self.name}.png', File(buffer), save=False)
        super().save(*args, **kwargs)
