from django.db import models


class ExampleManager(models.Manager):
    def create(self, **kwargs):
        example = super().create(**kwargs)
        return example


class Example(models.Model):
    def __str__(self):
        return f"Example Item {self.id}: {self.wow}"

    objects = ExampleManager()

    class Meta:
        ordering = ["id"]

    wow = models.BooleanField()
