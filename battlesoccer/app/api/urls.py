from django.urls import include, path
from rest_framework.routers import DefaultRouter
from app.api.views import (TeamViewSet,MatchplayedViewSet,
PlayerLikeAPIView,HighlightsViewSet,ContestViewSet,AvatarUpdateView,TeamRankViewSet,PlayerViewSet,PlayerpicUpdateView)

router = DefaultRouter()
router.register(r"team", TeamViewSet, basename="team")
router.register(r"player", PlayerViewSet, basename="player")
router.register(r"contest", ContestViewSet, basename="contest")


urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update"),
    path("highlights/", HighlightsViewSet.as_view(), name="highlights"),
    path("teamrank/", TeamRankViewSet.as_view(), name="teamrank"),
    path("matchplayed/", MatchplayedViewSet.as_view(), name="matchplayed"),
    path("playerpic/<int:pk>/", PlayerpicUpdateView.as_view(), name="playerpic-update"),
    path("playerlike/<int:pk>/like/",PlayerLikeAPIView.as_view(), name="player-like"),
]