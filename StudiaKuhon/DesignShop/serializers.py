from abc import ABC
from rest_framework import serializers

from .models import Product


class PhotoListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.photo


class TagListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return value.title


class ProductSerializer(serializers.ModelSerializer):
    # photos = PhotoListingField(many=True, read_only=True)
    styles = TagListingField(many=True, read_only=True)
    materials = TagListingField(many=True, read_only=True)
    palette = TagListingField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description_shorted', 'description_full', 'main_photo', 'photos', 'handle', 'styles',
                  'materials', 'palette', 'show',)
