from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'produto', views.ProdutoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("produtos_api", include(router.urls)),

]
