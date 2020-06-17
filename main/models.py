from django.db import models
from django.db.models import CharField, Case, When, Value as V
from django.db.models.functions import Concat, Cast, LPad


class CommentManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset().annotate(
            _sort_key=Case(
                When(
                    parent__isnull=True,
                    then=self.get_sort_key_expr('id', V('0'))
                ),
                When(
                    parent__isnull=False,
                    then=self.get_sort_key_expr('parent', 'id')
                ),
            )
        )
        queryset = queryset.order_by('_sort_key')
        return queryset

    @staticmethod
    def get_sort_key_expr(value_left, value_right, digit_count=10):
        return Concat(
            LPad(
                Cast(value_left, output_field=CharField()),
                digit_count,
                V('0')
            ),
            V('_'),
            LPad(
                Cast(value_right, output_field=CharField()),
                digit_count,
                V('0')
            )
        )


class Comment(models.Model):
    author_name = models.CharField(max_length=32)
    author_email = models.EmailField()
    text = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    objects = CommentManager()

    def sort_key(self):
        if self.parent:
            return f'{self.parent_id:0>10}_{self.id:0>10}'
        return f'{self.id:0>10}_0000000000'
