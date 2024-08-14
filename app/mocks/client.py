from faker import Faker
from ..common import utils

def client_data_mock(chosen_faker:Faker = None) -> dict:
    faker = chosen_faker if chosen_faker else utils.get_random_faker()
    return {
        'client_address': utils.get_random_address(faker),
        'client_dni': utils.get_random_sequence(),
        'client_name': utils.get_random_name(faker),
        'client_phone': utils.get_random_phone(faker)
    }