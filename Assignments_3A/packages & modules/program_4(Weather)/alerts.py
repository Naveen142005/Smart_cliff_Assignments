def check_extreme(weather_data):
    temp = weather_data[0]
    rain = weather_data[1]

    if temp >= 38:
        print('Heatwave warning')
    elif rain >= 70:
        print('Heavy rain warning')
    else:
        print('Usual weather')