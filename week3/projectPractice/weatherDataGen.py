import random
def get_random_weather_data():
    temp = random.uniform(-50, 50)
    weather = {
        'temp': temp,
        'feels_like': random.uniform(temp - 10, temp + 10),
        'humidity': random.randint(0, 100),
        'pressure': random.randint(990, 1010)
    }
    return weather

weather_list = []
for _ in range(100):
    weather_list.append(get_random_weather_data())
print(weather_list)