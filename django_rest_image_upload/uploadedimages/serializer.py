from rest_framework import serializers
from .models import UserImage


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ('pk', 'title', 'image', 'thumbnail')

    # def get_thumb(self, obj):
    #     if bool(obj.image):
    #         return self.context['request'].build_absolute_uri(obj.image.url)
    #     return ''
