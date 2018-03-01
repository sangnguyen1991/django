from django.db import models

class Users(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active')