from django.db import models


class ExampleManager(models.Manager):
    def create(self, **kwargs):
        example = super().create(**kwargs)
        return example


class Example(models.Model):
    def __str__(self):
        return f"Example Item {self.id}: {self.example_field}"

    objects = ExampleManager()

    class Meta:
        ordering = ["id"]

    class Choices(models.TextChoices):
        LOL = "LOL"
        GG = "GG"

    example_field = models.CharField(
        max_length=20, choices=Choices.choices, default=Choices.LOL
    )
