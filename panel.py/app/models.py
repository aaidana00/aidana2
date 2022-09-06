from django.db import models


class News(models.Model):
    title = models.CharField(max_length=222)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='%Y/%m/%d')

    def __str__(self):
        return self.title