from django.db import models
from django.db.models import Max


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if self.order == 0:
            max_order = Category.objects.aggregate(Max('order'))['order__max']
            self.order = (max_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category', 'name'], name='unique_category_name')
        ]
        ordering = ['order']

    def save(self, *args, **kwargs):
        if self.order == 0:
            max_order = Subcategory.objects.filter(category=self.category).aggregate(Max('order'))['order__max']
            self.order = (max_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} → {self.name}"


class MenuItem(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='menu_photos/', blank=True)
    subcategory = models.ForeignKey(Subcategory, related_name='menu_items', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if self.order == 0:
            max_order = MenuItem.objects.filter(subcategory=self.subcategory).aggregate(Max('order'))['order__max']
            self.order = (max_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
