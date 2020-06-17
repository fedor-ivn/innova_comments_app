from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    sort_key = serializers.CharField(read_only=True)

    class Meta:
        model = models.Comment
        fields = '__all__'

    def validate(self, data):
        parent = data.get('parent')
        if parent and parent.parent:
            raise serializers.ValidationError(
                'Parent comment must not have parent'
            )
        return data
