from rest_framework import viewsets
from .models import Image
from .serializer import ImageSerializer


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
