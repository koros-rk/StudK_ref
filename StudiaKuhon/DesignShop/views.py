# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
# from rest_framework.response import Response
from .models import *
from .serializers import ProductSerializer
# from .filters import ProductFilter
from Utils.permissions import ReadOnly, IsAdminUser
# from .paginations import StandardResultsSetPagination


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = ProductFilter
    permission_classes = [IsAdminUser | ReadOnly]
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Product.objects.all().filter(show=True)
        return queryset
