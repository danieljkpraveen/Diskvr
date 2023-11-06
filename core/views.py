from django.shortcuts import render, redirect
from django.template import RequestContext

from inventory.models import NeonLights
from .forms import SignUpForm



def index(request):
    # this view renders the index page

    items = NeonLights.objects.all()[0:15]
    return render(
        request,
        "core/index.html",
        {
            'items': items,
        }
    )


def signup(request):
    # this view renders the sign up page

    errors = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            errors = form.errors
    form = SignUpForm()
    return render(
        request,
        'core/signup.html',
        {'form': form, 'errors': errors}
    )


def handler404(request, exception):
    response = render(
        request,
        'core/404.html',
        {}
    )
    response.status_code = 404

    return response