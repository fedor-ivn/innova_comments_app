from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'

    def validate(self, data):
        parent = data.get('parent')
        if parent.parent is not None:
            raise serializers.ValidationError(
                'Parent comment must not have parent'
            )
        return data
