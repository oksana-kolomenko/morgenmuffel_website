from django.db import models

from django.db import models

class TeamMember(models.Model):
    nickname = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team_photos/', blank=True)
    order = models.PositiveIntegerField(default=0, unique=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.nickname} ({self.position})"
