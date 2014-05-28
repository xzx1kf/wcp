from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from prediction.models import Match

@login_required
def predictions(request):
    matches_list = Match.objects.all().order_by('datetime')
    context = {'matches_list': matches_list}
    return render(request, 'prediction/index.html', context)
