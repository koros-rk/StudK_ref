from rest_framework import viewsets
from .models import Style, Palette, Photos, Material
from .sezializers import StyleSerializer, PaletteSerializer, PhotoSerializer, MaterialSerializer
from .permissions import ReadOnly, IsAdminUser


class StylesViewSet(viewsets.ModelViewSet):
    serializer_class = StyleSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_queryset(self):
        queryset = Style.objects.all()
        return queryset


class MaterialsViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_queryset(self):
        queryset = Material.objects.all()
        return queryset


class PaletteViewSet(viewsets.ModelViewSet):
    serializer_class = PaletteSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_queryset(self):
        queryset = Palette.objects.all()
        return queryset


class PhotosViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    def get_queryset(self):
        queryset = Photos.objects.all()
        return queryset


sets = [("styles", StylesViewSet), ("materials", MaterialsViewSet), ("palletes", PaletteViewSet),
        ("photos", PhotosViewSet)]
