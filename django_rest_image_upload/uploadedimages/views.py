from rest_framework import viewsets, permissions
from .models import UserImage
from .serializer import UserImageSerializer


class ImageView(viewsets.ModelViewSet):
    queryset = UserImage.objects.all()
    serializer_class = UserImageSerializer
    # permission_classes = (permissions.UseBasicTier,)

    # @action(....)
    # def..() -> l=exp link