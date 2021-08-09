from django.db import models

# Create your models here.

class Todomodel(models.Model):
    Title = models.CharField(max_length=100)
    Task = models.TextField()
    is_done = models.BooleanField(default=False)
    def __str__(self):
        return self.Title
    class Meta:
        ordering = ['-id']

    
    