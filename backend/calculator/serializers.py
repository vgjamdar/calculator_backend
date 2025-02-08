from rest_framework import serializers


class MathQuerySerializer(serializers.Serializer):
    query = serializers.CharField(max_length=255, allow_null=False, allow_blank=False, required=True)
