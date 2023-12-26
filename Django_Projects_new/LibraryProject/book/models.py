from django.db import models

# Create your models here.

class CustomBookManager(models.Manager):
    def get_active_objects(self):
        return self.filter(isdeleted=False)
    
    def get_inactive_objects(self):
        return self.filter(isdeleted=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pulication_date = models.DateField()
    isdeleted = models.BooleanField(default=False)
    price = models.IntegerField()
    objects = CustomBookManager()

    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
