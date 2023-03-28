from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.BigIntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
