from django.db import models
from brands.models import BaseModel

class Color(BaseModel):
    hex_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

