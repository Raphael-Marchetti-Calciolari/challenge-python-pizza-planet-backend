from app.test.utils.functions import get_random_size_name, get_random_price


def test_create_size_service(create_size):
    size = create_size.json
    assert(create_size.status.startswith('200'))
    assert(size['_id'])
    assert(size['name'])
    assert(size['price'])


def test_update_size_service(client, create_size, size_uri):
    current_size = create_size.json
    update_data = {**current_size, 'name': get_random_size_name().capitalize(), 'price': get_random_price(1.99, 30)}
    response = client.put(size_uri, json=update_data)
    assert(response.status.startswith('200'))
    updated_size = response.json
    for param, value in update_data.items():
        assert(updated_size[param] == value)


def test_delete_size_by_id_service(client, create_size, size_uri):
    current_size = create_size.json
    response = client.delete(f'{size_uri}id/{current_size["_id"]}')
    assert(response.status.startswith('200'))
    response = client.delete(size_uri, json=current_size)
    assert(response.status.startswith('4'))


def test_get_size_by_id_service(client, create_size, size_uri):
    current_size = create_size.json
    response = client.get(f'{size_uri}id/{current_size["_id"]}')
    assert(response.status.startswith('200'))
    returned_size = response.json
    for param, value in current_size.items():
        assert(returned_size[param] == value)


def test_get_sizes_service(client, create_sizes, size_uri):
    response = client.get(size_uri)
    assert(response.status.startswith('200'))
    returned_sizes = {size['_id']: size for size in response.json}
    for size in create_sizes:
        assert(size['_id'] in returned_sizes)
