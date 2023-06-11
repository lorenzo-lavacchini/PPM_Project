from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("recipes-detail",kwargs={"pk": self.pk})
    def __str__(self):
        return self.title