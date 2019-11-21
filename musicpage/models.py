from django.db import models
from django.urls import reverse
import uuid


class Review(models.Model):
    nombre=models.CharField(max_length=20, primary_key=True)
    email=models.EmailField()
    review=models.TextField(max_length=300)
    class Meta:
        ordering =['nombre']
    
    
    def get_absolute_url(self):
        return reverse('review-detail',args=[str(self.nombre)])

    def __str__(self):
        return f'{self.nombre},{self.email},{self.review}'

    
    
     
