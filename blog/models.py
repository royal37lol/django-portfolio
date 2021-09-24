from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.title
