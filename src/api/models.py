from PIL import Image, ImageOps
from django.db import models


class Beard(models.Model):
    image = models.ImageField(upload_to="beards/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Beard"
        verbose_name_plural = "Beards"

    def resize_image(
            self,
            width: int,
            height: int,
            colored: bool = True
    ) -> Image:
        image = Image.open(self.image.open("rb"))
        resized_image = image.resize((width, height))
        if not colored:
            resized_image = ImageOps.grayscale(resized_image)
        return resized_image

    def __str__(self) -> str:
        return f"Beard: id<{self.pk}>"
