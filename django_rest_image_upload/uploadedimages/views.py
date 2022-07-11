from rest_framework import viewsets
from .models import UploadImage
from .serializer import UserImageSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class UserImageView(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UserImageSerializer

    @action(methods=['get'], detail=False)
    def user_img(self, request):
        user_img = self.get_queryset().filter_by(user=request.user)
        serializer = self.get_serializer_class()(user_img, many=True)
        return Response(serializer.data)
