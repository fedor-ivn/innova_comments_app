from django.db import models
from mptt import models as mptt_models


class MPTTComment(mptt_models.MPTTModel):
    author_name = models.CharField(max_length=32)
    author_email = models.EmailField()
    text = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = mptt_models.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
