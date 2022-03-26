from django.urls import path, include
from rest_framework import routers

from .views import FollowViewSet, PostViewSet, CommentViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register("v1/posts", PostViewSet)
router.register(
    r"v1/posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="comments",
)
router.register("v1/groups", GroupViewSet)
router.register("v1/follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
