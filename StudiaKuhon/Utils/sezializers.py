from rest_framework import serializers
from .models import Style, Palette, Photos, Material


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ('title', )


class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = ('title', )


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('title', )


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ('photo',)
