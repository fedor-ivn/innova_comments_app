from django.db import models


class Comment(models.Model):
    author_name = models.CharField(max_length=32)
    author_email = models.EmailField()
    text = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
