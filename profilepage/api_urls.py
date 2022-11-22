from rest_framework import viewsets
from rest_framework import routers
from profilepage.api_views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
urlpatterns = router.urls
