from rest_framework import generics, mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import generics, status, viewsets


from app.api.permissions import IsOwnerOrReadOnly, IsOwnProfileOrReadOnly
from app.api.serializers import (TeamSerializer,ContestSerializer,HighlightsSerializer,TeamRankSerializer,TeamAvatarSerializer,
                                      PlayerSerializer,PlayerAvatarSerializer,MacthplayedSerializer,
                                      )
from app.models import team,contestteam,player,teamrank,highlights,match



class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = TeamAvatarSerializer

    def get_object(self):
        team_object = self.request.user.team
        return team_object


class PlayerpicUpdateView(generics.UpdateAPIView):
    serializer_class = PlayerAvatarSerializer

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        player_object = get_object_or_404(player,pk=pk)
        return player_object



class TeamViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsOwnProfileOrReadOnly]



class ContestViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = contestteam.objects.all()
    serializer_class = ContestSerializer



class TeamRankViewSet(generics.ListAPIView):
    queryset = teamrank.objects.all().order_by('-match_won')
    lookup_field = "team_a"
    serializer_class = TeamRankSerializer


class MatchplayedViewSet(generics.ListAPIView):
    queryset = match.objects.all()
    lookup_field = "team_a"
    serializer_class = MacthplayedSerializer


class HighlightsViewSet(generics.ListAPIView):
    queryset = highlights.objects.all()
    lookup_field = "teamname"
    serializer_class = HighlightsSerializer



class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    lookup_field = "id"
    filter_backends = [SearchFilter]
    search_fields = ["player"]


    def get_queryset(self):
        queryset = player.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(teamname__user__username=username)
        return queryset


    def perform_create(self, serializer):
        teamname = self.request.user.team
        serializer.save(teamname=teamname)


class PlayerLikeAPIView(APIView):
    """Allow users to add/remove a like to/from an answer instance."""
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]


    def delete(self, request, pk):
        """Remove request.user from the voters queryset of an answer instance."""
        players = get_object_or_404(player, pk=pk)
        user = request.user

        players.voters.remove(user)
        players.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(players, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        """Add request.user to the voters queryset of an answer instance."""
        players = get_object_or_404(player, pk=pk)
        user = request.user

        players.voters.add(user)
        players.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(players, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

