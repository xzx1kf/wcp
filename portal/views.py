from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from portal.forms import UserForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    #return HttpResponse("portal says hello world!")
    context = RequestContext(request)
    return render_to_response('portal/index.html',{}, context)

def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render_to_response(
            'portal/register.html',
            {'user_form': user_form, 'registered': registered},
            context)

def user_login(request):
    # Obtain the context for the user's request
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This informaiton is obtained fromm the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combintaion is valid = a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # IF we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value, no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/portal/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your WCP account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('portal/login.html', {}, context)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/portal/')

