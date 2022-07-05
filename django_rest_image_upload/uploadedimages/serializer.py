from rest_framework import serializers
from .models import UploadImage


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ('pk', 'title', 'image', 'thumbnail', 'binary_img', 'time_link_expires', 'time_from_image_upload')
        read_only_fields = ('thumbnail', 'binary_img',)

    # def get_thumb(self, obj):
    #     if bool(obj.image):
    #         return self.context['request'].build_absolute_uri(obj.image.url)
    #     return ''
