from django.contrib import admin
from .models import player,team,match,contestteam,teamrank,highlights

admin.site.register(team)
admin.site.register(player)
admin.site.register(match)
admin.site.register(teamrank)
admin.site.register(highlights)
admin.site.register(contestteam)

