from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r"bdomarket", ItemViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("time/", date_time),    
    path("item/", item_test_view),
    path("import/", simple_upload),    
]
