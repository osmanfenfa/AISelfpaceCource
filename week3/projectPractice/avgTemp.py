import random
def get_random_weather_data():
    temp = random.uniform(-50, 50)

    return {
        'temp': temp,
        'feels_like': random.uniform(temp - 10, temp + 10),
        'humidity': random.randint(0, 100),
        'pressure': random.randint(990, 1010)
    }

def get_average_temperature(weather_data):
    total_temp = 0
    for data in weather_data:
        total_temp += data['temp']

    average = total_temp / len(weather_data)
    return average

weather_list = []

for _ in range(100):
    weather_list.append(get_random_weather_data())
avg_temp = get_average_temperature(weather_list)
print("Average Temperature:", avg_temp)