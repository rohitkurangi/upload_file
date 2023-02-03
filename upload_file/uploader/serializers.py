from rest_framework import serializers
from .models import Upload


class UploadSerializer(serializers.ModelSerializer):
    upload_file = serializers.FileField()

    class Meta:
        model = Upload
        fields = ('__all__')

    def create(self, validated_data):
        """
        Create and return a new `Students` instance, given the validated data.
        """
        return Upload.objects.create(**validated_data)