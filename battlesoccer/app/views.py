from django.shortcuts import render
from .forms import MatchForm,TeamrankForm
from .models import match,teamrank
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Sum

# Create your views here.

def matchplayed(request):
    form = MatchForm(request.POST or None, request.FILES or None)
    form1 = TeamrankForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        match0 = form.save(commit=False)
        team_a = form.cleaned_data['team_a']
        team_b = form.cleaned_data['team_b']
        team_goal_a = form.cleaned_data['team_a_goals']
        team_goal_b = form.cleaned_data['team_b_goals']
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        if team_goal_a > team_goal_b:
            match0.winner = team_a;
        else:
            match0.winner = team_b
        match0.save()
        form = MatchForm()
        match1 = form.save(commit=False)
        match1.team_a = team_b
        match1.team_b = team_a
        match1.team_a_goals = team_goal_b
        match1.team_b_goals = team_goal_a
        match1.date = date
        match1.time = time
        if team_goal_a > team_goal_b:
            match1.winner = team_a
        else:
            match1.winner = team_b
        match1.save()
        if teamrank.objects.filter(teamname=team_a).exists():
            instance1 = get_object_or_404(teamrank, teamname=team_a)
            formone=TeamrankForm(request.POST or None, request.FILES or None,instance=instance1,prefix="form1")
        else:
            formone=TeamrankForm(request.POST or None, request.FILES or None,prefix="form1")
        user = formone.save(commit=False)
        user.teamown = team_a
        user.teamname =str(team_a)
        goal1=match.objects.filter(team_a=team_a).aggregate(sum=Sum('team_a_goals'))['sum']
        user.teamgoals = goal1
        matchtotal1 = match.objects.filter(team_a=team_a).count()
        user.matchs_played = matchtotal1
        matchwon1 = match.objects.filter(winner=team_a,team_a=team_a).count()
        user.match_won = matchwon1
        matchlost1 = matchtotal1 - matchwon1
        user.match_lost = matchlost1
        user.save()
        if teamrank.objects.filter(teamname=team_b).exists():
            instance1 = get_object_or_404(teamrank, teamname=team_b)
            formone=TeamrankForm(request.POST or None, request.FILES or None,instance=instance1,prefix="form1")
        else:
            formone=TeamrankForm(request.POST or None, request.FILES or None,prefix="form1")
        user = formone.save(commit=False)
        user.teamown = team_b
        user.teamname =str(team_b)
        user.teamgoals =match.objects.filter(team_a=team_b).aggregate(sum=Sum('team_a_goals'))['sum']
        matchtotal=match.objects.filter(team_a=team_b).count()
        user.matchs_played=matchtotal
        matchwon=match.objects.filter(winner=team_b,team_a=team_b).count()
        user.match_won=matchwon
        matchlost=matchtotal-matchwon
        user.match_lost=matchlost
        user.save()
    context = {
        'form': form,
    }
    return render(request, 'match.html', context)

