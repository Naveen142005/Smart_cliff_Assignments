from forecast import get_forcast
from temperature import celsius_to_fahrenheit
from alerts import check_extreme

def main():
    city = input()
    weather_data = get_forcast()
    fahrenheit = celsius_to_fahrenheit(weather_data[0])

    print(city)
    print(f'Temp = {weather_data[0]}°C ({fahrenheit}°F)')
    print (f'Rain = {weather_data[1]}%')

    check_extreme(weather_data)
if __name__ == "__main__":
    main()