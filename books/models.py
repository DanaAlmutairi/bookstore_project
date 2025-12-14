from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
            verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    isbn = models.CharField(max_length=20, unique=True)
    published_at = models.DateField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='books', blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
