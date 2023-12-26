from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mob_num = models.IntegerField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name}"
    
