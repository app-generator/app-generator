# serializers.py
from rest_framework import serializers


class CSVUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        # Check if the uploaded file is a CSV
        if not value.name.endswith(".csv"):
            raise serializers.ValidationError("This is not a CSV file.")
        return value


class CSVProcessorSerializer(serializers.Serializer):
    file = serializers.CharField()
    fields = serializers.JSONField()
