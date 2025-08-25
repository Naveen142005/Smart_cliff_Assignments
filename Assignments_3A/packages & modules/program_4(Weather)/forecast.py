import random
def get_forcast():
    celsius = random.randint(-5, 45)

    if celsius >= 35:
        rain_chance = random.randint(0, 20)
    elif 20 <= celsius < 35:
        rain_chance = random.randint(20, 60)
    elif 10 <= celsius < 20:
        rain_chance = random.randint(40, 80)
    else:
        rain_chance = random.randint(60, 100)

    return [celsius, rain_chance]
