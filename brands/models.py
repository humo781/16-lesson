from django.db import models

class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Brand(BaseModel):
    desc = models.TextField()

    def __str__(self):
        return self.name
