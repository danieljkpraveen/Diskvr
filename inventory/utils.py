from .models import Order


def orders_list_data(user):
    completed_orders = None
    working_orders = None
    client_orders = None

    if user.is_superuser:
        completed_orders = Order.objects.filter(
            complete=True
        ).order_by('-order_id')
        working_orders = Order.objects.filter(
            complete=False
        ).order_by('-order_id')
    else:
        client_orders = Order.objects.filter(
            username=user.username,
            complete=False
        ).order_by('-order_id')

    return_data = {}
    if completed_orders:
        return_data['completed_orders'] = completed_orders
    if working_orders:
        return_data['working_orders'] = working_orders
    if client_orders:
        return_data['client_orders'] = client_orders
    
    return return_data