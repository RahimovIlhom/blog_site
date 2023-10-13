from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='sarlavha')
    summary = models.CharField(max_length=500)
    body = RichTextField()
    image = models.ImageField(upload_to='images/', blank=True)
    at_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.pk)])


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.comment}"

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.blog.pk)])
