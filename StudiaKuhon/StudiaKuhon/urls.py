from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Utils.views import sets
from DesignShop.views import ProductViewSet
from .yasg import urlpatterns as SwaggerURL

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
for title, VSet in sets:
    router.register(r""+title, VSet, basename=title)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
]

urlpatterns += SwaggerURL
