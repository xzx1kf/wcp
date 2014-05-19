from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.
def main_page(request):
    return render_to_response('index.html')
