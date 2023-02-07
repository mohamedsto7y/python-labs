from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_name = models.CharField(max_length=100)
    blog_category = models.ForeignKey("Category",on_delete=models.CASCADE)
    blog_text = models.TextField()

class Category(models.Model):
    cat_name = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_name