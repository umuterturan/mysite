from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_adress = models.EmailField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

   
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.CharField(max_length=80)
    date = models.TimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    date2 = models.DateField(auto_now=True, null=True)
      
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name = "posts")
    tags = models.ManyToManyField(Tag)