import random
import string
from typing import Any, Union
from faker import Faker

fakeAR = Faker('es_AR')
fakeBR = Faker('pt_BR')
fakeUS = Faker('en_US')


fakers = [fakeAR, fakeBR, fakeUS]


ingredients = [
    "pepperoni", "mushrooms", "onions",
    "sausage", "bacon", "black olives",
    "green peppers", "pineapple", "spinach",
    "ham", "chicken", "tomatoes",
    "garlic", "oregano", "anchovies",
    "salami", "prosciutto", "mozzarella cheese",
    "parmesan cheese", "cheddar cheese", "jalapenos"
]


sizes = [
    "mini", "extra small", "small",
    "child size", "medium", "personal",
    "regular", "single serving", "half size",
    "large", "extra large", "jumbo",
    "family size", "party size", "giant",
    "king size", "double size"
]


def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)


def get_random_faker() -> Faker:
    return get_random_choice(fakers)


def get_random_string() -> str:
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    return ''.join(letters[:10])


def get_random_choice(choices: Union[tuple, list]) -> Any:
    return random.choice(choices)


def get_random_choices(choices: Union[tuple, list]) -> Any:
    n_choices = random.randint(1, len(choices))
    return random.choices(choices, k=n_choices)


def get_random_price(lower_bound: float, upper_bound: float) -> float:
    return round(random.uniform(lower_bound, upper_bound), 2)


def get_random_sequence(length: int = 10) -> str:
    digits = list(map(str, range(10)))
    sequence = [digits[random.randint(0, 9)] for _ in range(length)]
    return ''.join(sequence)


def get_random_phone(chosen_faker:Faker = None) -> str:
    faker = chosen_faker if chosen_faker else get_random_faker()
    return faker.phone_number()


def get_random_address(chosen_faker:Faker = None) -> str:
    faker = chosen_faker if chosen_faker else get_random_faker()
    address = faker.address()
    address = address.replace('\n', ', ')
    address = address.replace(' /', ',')
    return address


def get_random_name(chosen_faker:Faker = None) -> str:
    faker = chosen_faker if chosen_faker else get_random_faker()
    return faker.name()


def get_random_ingredient_name() -> str:
    if len(ingredients) <= 0: return get_random_string()
    choice = get_random_choice(ingredients)
    ingredients.remove(choice)
    return choice


def get_random_size_name() -> str:
    if len(ingredients) <= 0: return get_random_string()
    choice = get_random_choice(sizes)
    sizes.remove(choice)
    return choice