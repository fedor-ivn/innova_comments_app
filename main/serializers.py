from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    sort_key = serializers.CharField(read_only=True)

    class Meta:
        model = models.MPTTComment
        fields = '__all__'
