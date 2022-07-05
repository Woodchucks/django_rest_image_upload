from rest_framework import viewsets, permissions
from .models import UploadImage
from .serializer import UserImageSerializer


class UserImageView(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UserImageSerializer


# permission_classes = (permissions.UseBasicTier,)

    # @action(....)
    # def..() -> l=exp link
