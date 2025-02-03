from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from brands.models import Brand, BaseModel
from colors.models import Color
from catalogs.models import Catalog

class Product(BaseModel):
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_image/')
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('products:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
