from django.db import models
from brands.models import BaseModel

class Catalog(BaseModel):
    desc = models.TextField()

    def __str__(self):
        return self.name

