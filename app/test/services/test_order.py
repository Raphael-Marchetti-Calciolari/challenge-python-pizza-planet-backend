

def test_create_order_service(create_order):
    order = create_order.json
    assert(create_order.status.startswith('200'))
    assert(order['_id'])
    assert(order['client_address'])
    assert(order['client_dni'])
    assert(order['client_name'])
    assert(order['client_phone'])
    assert(order['date'])
    assert(order['total_price'])
    assert(order['size'])
    assert(order['ingredient_detail'])
    assert(order['beverage_detail'])


def test_update_order_service(client, order_uri):
    response = client.put(order_uri)
    assert(response.status.startswith('4'))


def test_get_order_by_id_service(client, create_order, order_uri):
    print(f'Current order: {create_order}')
    current_order = create_order.json
    response = client.get(f'{order_uri}id/{current_order["_id"]}')
    assert(response.status.startswith('200'))
    returned_order = response.json
    for param, value in current_order.items():
        assert(returned_order[param] == value)


def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    assert(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}
    for order in create_orders:
        assert(order['_id'] in returned_orders)