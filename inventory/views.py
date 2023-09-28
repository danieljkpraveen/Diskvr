from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import NeonLights
from .forms import EditItemForm, NewItemForm


def detail(request, pk):
    # this view is for the details page

    item = get_object_or_404(NeonLights, pk=pk)
    related_items = NeonLights.objects.exclude(pk=pk).order_by('?')[:6]
    return render(
        request,
        'inventory/detail.html',
        {
            'item': item,
            'related_items': related_items,
        }
    )


def items(request):
    # this view is for search items

    query = request.GET.get('query', '')
    items = NeonLights.objects.all()

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(
        request,
        'inventory/items.html',
        {
            'items': items,
            'query': query,
        }
    )


@login_required
def new(request):
    # this view is to create new item

    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('inventory:detail', pk=item.id)
    
    else:
        form = NewItemForm()
    
    return render(
        request,
        'inventory/form.html',
        {
            'form': form,
            'title': 'New Item',
        }
    )


@login_required
def delete(request, pk):
    # this view is to delete item

    item = get_object_or_404(NeonLights, pk=pk, created_by=request.user)
    item.delete()
    return redirect('/')


@login_required
def edit(request, pk):
    # this view is to edit item

    item = get_object_or_404(NeonLights, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('inventory:detail', pk=item.id)
    
    else:
        form = EditItemForm(instance=item)
    
    return render(
        request,
        'inventory/form.html',
        {
            'form': form,
            'title': 'Edit Item',
        }
    )


@login_required
def order(request, pk):
    # this view is to track orders made by customers

    if request.method == 'POST':
        print(pk)
        return render(request, 'inventory/orders.html')
    else:
        return render(request, 'inventory/orders.html')
