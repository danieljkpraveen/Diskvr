from .models import Order


def orders_list_data(user):
    return_data = None

    if user.is_superuser:
        return_data = Order.objects.filter(
            status='IP'
        ).order_by('-order_id')
    else:
        return_data = Order.objects.filter(
            username=user.username,
            status__in=['IP', 'NA']
        ).order_by('-order_id')

    return return_data


def pending_orders(user):
    return_data = None

    if user.is_superuser:
        return_data = Order.objects.filter(
            status='NA'
        ).order_by('-order_id')
    
    return return_data


def closed_orders(user):
    completed_orders = None

    # below code is to view attributes of an object
    # attributes = dir(user)
    # print(attributes)

    if user.is_superuser:
        completed_orders = Order.objects.filter(
            status='CO'
        ).order_by('-order_id')
    else:
        completed_orders = Order.objects.filter(
            username=user.username,
            status='CO'
        ).order_by('-order_id')
    
    return completed_orders