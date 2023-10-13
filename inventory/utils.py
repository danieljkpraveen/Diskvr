from .models import Order


def orders_list_data(user):
    working_orders = None
    client_orders = None

    if user.is_superuser:
        working_orders = Order.objects.filter(
            complete=False
        ).order_by('-order_id')
    else:
        client_orders = Order.objects.filter(
            username=user.username,
            complete=False
        ).order_by('-order_id')

    return_data = {}
    if working_orders:
        return_data['working_orders'] = working_orders
    if client_orders:
        return_data['client_orders'] = client_orders
    
    return return_data


def closed_orders(user):
    closed_orders_data = None

    # below code is to view attributes of an object
    # attributes = dir(user)
    # print(attributes)

    if user.is_superuser:
        closed_orders_data = Order.objects.filter(
            complete=True
        ).order_by('-order_id')
    else:
        closed_orders_data = Order.objects.filter(
            username=user.username,
            complete=True
        ).order_by('-order_id')
    
    return closed_orders_data