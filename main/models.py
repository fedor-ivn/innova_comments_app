from django.db import models
from django.db.models import CharField, Case, When, Value as V
from django.db.models.functions import Concat


class CommentManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset().annotate(
            sort_key=Case(
                When(
                    parent__isnull=True,
                    then=Concat('id', V('_0'), output_field=CharField())
                ),
                When(
                    parent__isnull=False,
                    then=Concat('parent', V('_'), 'id', output_field=CharField())
                ),
                output_field=CharField()
            )
        )
        queryset = queryset.order_by('sort_key')
        return queryset


class Comment(models.Model):
    author_name = models.CharField(max_length=32)
    author_email = models.EmailField()
    text = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    objects = CommentManager()
