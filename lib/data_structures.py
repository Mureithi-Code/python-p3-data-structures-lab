spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [x['name'] for x in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [y for y in spicy_foods if y['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for z in spicy_foods:
        hot = '🌶' * z['heat_level']
        print(f"{z['name']} ({z['cuisine']}) | Heat Level: {hot}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for a in spicy_foods:
        if a['cuisine'] == cuisine:
            return a
    return None
print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for z in spiciest_foods:
        hot = '🌶' * z['heat_level']
        print(f"{z['name']} ({z['cuisine']}) | Heat Level: {hot}")

def get_average_heat_level(spicy_foods):
    total_heat = sum(c['heat_level'] for c in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods > 0:
        return total_heat // num_foods
    else:
        return 0

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
