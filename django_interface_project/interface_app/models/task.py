from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(name="名称", blank=False,
                            max_length=200, default="")
    description = models.CharField(name="描述", blank=False,
                                   max_length=2000, default="")
