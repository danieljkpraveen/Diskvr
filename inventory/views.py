from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone

from core.models import UserProfile
from .models import NeonLights, Order
from .forms import EditItemForm, NewItemForm

from .utils import orders_list_data, closed_orders


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
        items = items.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

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

    item = get_object_or_404(
        NeonLights,
        pk=pk,
        created_by=request.user
    )
    item.delete()
    return redirect('/')


@login_required
def edit(request, pk):
    # this view is to edit item

    item = get_object_or_404(
        NeonLights,
        pk=pk,
        created_by=request.user
    )
    if request.method == 'POST':
        form = EditItemForm(
            request.POST,
            request.FILES,
            instance=item
        )
        
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
    # this view is to generate order id and create new orders

    product = NeonLights.objects.get(id=pk)
    user_profile = UserProfile.objects.get(user=request.user)
    
    order_id = timezone.now().strftime("%m%d%Y%H%M%S%f")
    product_name = product.name
    product_price = product.price
    product_image_path = str(product.image)
    username = request.user.username
    email = request.user.email
    phone_no = user_profile.phone_number

    return_data = {
        'order_id': order_id,
        'product_id': pk,
        'product_name': product_name,
        'product_price': product_price,
        'product_image_path': product_image_path,
        'username': username,
        'email': email,
        'phone_no': phone_no
    }

    Order.objects.create(
        order_id=order_id,
        product_name=product_name,
        price=product_price,
        product_image_path=product_image_path,
        username=username,
        email=email,
        phone_number=phone_no
    )

    return render(
        request,
        'inventory/order.html',
        {'order': return_data}
    )


@login_required
def order_list(request):
    # this view is to track orders made by customers

    user = request.user

    return_data = orders_list_data(user)

    if request.method == 'POST':
        checkbox_value = request.POST.get('myCheckbox')
        completed_order_id = request.POST.get('order_id')

        if checkbox_value == 'checked':
            completed_order = Order.objects.get(pk=completed_order_id)
            completed_order.complete = True
            completed_order.save()

            return_data = orders_list_data(user)

            return render(
                request,
                'inventory/orders_list.html',
                {'orders': return_data}
            )

    return render(
        request,
        'inventory/orders_list.html',
        {'orders': return_data}
    )


@login_required
def completed_orders(request):
    # this view is to get completed orders

    user = request.user

    return_data = closed_orders(user)

    if request.method == 'POST':
        checkbox_value = request.POST.get('myCheckbox')
        completed_order_id = request.POST.get('order_id')

        if checkbox_value is None:
            completed_order = Order.objects.get(pk=completed_order_id)
            completed_order.complete = False
            completed_order.save()

            return_data = closed_orders(user)

            return render(
                request,
                'inventory/closed_orders.html',
                {'orders': return_data}
            )

    return render(
        request,
        'inventory/closed_orders.html',
        {'orders': return_data}
    )