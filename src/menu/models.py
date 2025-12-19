from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category', 'name'], name='unique_category_name')
        ]

    def __str__(self):
        return f"{self.category.name} → {self.name}"


class MenuItem(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='menu_photos/', blank=True)
    subcategory = models.ForeignKey(Subcategory, related_name='menu_items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
