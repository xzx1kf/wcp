from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from prediction.models import Match, Prediction

@login_required
def predictions(request):
    matches = Match.objects.all().order_by('datetime')

    if request.method == 'POST':
        alldata = request.POST

        for m in matches:
            home_goals = alldata.get("home_goals_%s" % m.id)
            away_goals = alldata.get("away_goals_%s" % m.id)

            if len(home_goals) > 0 and len(away_goals) > 0:
                try:
                    p = Prediction.objects.get(match=m, user=request.user)
                    p.home_goals = int(home_goals)
                    p.away_goals = int(away_goals)
                    p.user = request.user
                    p.save()
                except:
                    p = Prediction(match=m, user=request.user, home_goals=int(home_goals), away_goals=int(away_goals))
                    p.save()

            return redirect("predictions")
    else:
        data = []

        for m in matches:
            p = Prediction.objects.filter(match=m, user=request.user)

            if p.exists():
                row = {
                    "id": m.id,
                    "home_team": m.home_team,
                    "home_goals": p[0].home_goals,
                    "away_goals": p[0].away_goals,
                    "away_team": m.away_team,
                    "datetime": m.datetime}
                data.append(row)
            else:
                row = {
                    "id": m.id,
                    "home_team": m.home_team,
                    "home_goals": "",
                    "away_goals": "",
                    "away_team": m.away_team,
                    "datetime": m.datetime}
                data.append(row)

        context = { "matches": data }

        return render(request, 'prediction/index.html', context)
