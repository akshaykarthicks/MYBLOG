from django.db import models
from datetime import datetime #for date and time

# Create your models here.
#models are used to create tables in the database
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=100000000)
    created_at=models.DateTimeField(default=datetime.now,blank=True) 
    
    