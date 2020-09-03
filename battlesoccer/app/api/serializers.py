from rest_framework import serializers
from app.models import team, player,teamrank,highlights,match,contestteam




class TeamAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = team
        fields = ("logo", "coverpic",)



class PlayerAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = player
        fields = ("pic",)

class TeamdataSerializer(serializers.ModelSerializer):
    coverpic = serializers.ImageField(read_only=True)
    logo = serializers.ImageField(read_only=True)



    class Meta:
        model = team
        fields = "__all__" 


class PlayerSerializer(serializers.ModelSerializer):

    teamname = serializers.StringRelatedField(read_only=True)
    pic = serializers.ImageField(read_only=True)
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    own = TeamdataSerializer(source='teamname',read_only=True)

    class Meta:
        model = player
        exclude = ["voters"]

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_likes_count(self, instance):
        return instance.voters.count()


class HighlightsSerializer(serializers.ModelSerializer):
    teamname = serializers.StringRelatedField(read_only=True)
    own = TeamdataSerializer(source='teamname',read_only=True)

    class Meta:
        model = highlights
        fields = "__all__"

class ContestSerializer(serializers.ModelSerializer):
    own = TeamdataSerializer(source='teamown',read_only=True)

    class Meta:
        model = contestteam
        fields = "__all__"

class MacthplayedSerializer(serializers.ModelSerializer):
    team_a = serializers.StringRelatedField(read_only=True)
    team_b = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = match
        fields = "__all__"
     

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    videos = HighlightsSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    coverpic = serializers.ImageField(read_only=True)
    logo = serializers.ImageField(read_only=True)
    belongs=MacthplayedSerializer(many=True, read_only=True)



    class Meta:
        model = team
        fields = "__all__"

class TeamdataSerializer(serializers.ModelSerializer):
    coverpic = serializers.ImageField(read_only=True)
    logo = serializers.ImageField(read_only=True)



    class Meta:
        model = team
        fields = "__all__" 


class TeamRankSerializer(serializers.ModelSerializer):
    own = TeamdataSerializer(source='teamown',read_only=True)

    class Meta:
        model = teamrank
        fields = ['teamname','teamgoals',
        'match_lost','matchs_played','match_won','own']

