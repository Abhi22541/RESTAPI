from django.db import models




class Film(models.Model):
    name = models.CharField(max_length=150)
    detail = models.CharField(max_length=255)
    release = models.BooleanField()




    def __str__(self) -> str:
        return self.name


# Create your models here.
