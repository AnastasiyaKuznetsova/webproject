from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()

my_object = MyModel(name = 'John', age = 30, email = 'john@example.com')
my_object.save()