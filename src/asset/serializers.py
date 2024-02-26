from rest_framework import serializers
from asset.models import Banner


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = [
            "title",
            "image",
        ]
