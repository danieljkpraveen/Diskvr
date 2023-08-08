from django.shortcuts import render, redirect

from inventory.models import Category, Inventory
from .forms import SignUpForm, LoginForm



def index(request):
    items = Inventory.objects.all()  # [0:10]
    categories = Category.objects.all()
    return render(
        request,
        "core/index.html",
        {
            'categories': categories,
            'items': items,
        }
    )


def signup(request):
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
