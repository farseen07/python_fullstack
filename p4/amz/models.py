from django.db import models

# Create your models here.
class student(models.Model):
    name =models.CharField(max_length=20)
    email =models.EmailField(unique=True)
    age =models.IntegerField()
    create_at =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

