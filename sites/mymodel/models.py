from django.db import models
class Comment(models.Model):
 
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
 
    def __str__(self):  
        return self.title