from rest_framework.generics import ListCreateAPIView

from . import models
from . import serializers


class CommentAPIView(ListCreateAPIView):
    queryset = models.MPTTComment.objects.all()
    serializer_class = serializers.CommentSerializer
