from django.db import models
import uuid
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.category_name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)

    def __str__(self):
        return self.book_title


class Student(models.Model):
    id = models.UUIDField(primary_key=True, max_length=200, default=uuid.uuid4(), editable=False)
    first_name = models.CharField(default="", max_length=200)
    last_name = models.CharField(default="", max_length=200)
    email = models.EmailField(default="", unique=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.email


