#24.24. WEATHER STATION DATA ANALYSIS

def get_max_min(readings):
    # take first values
    max_temp = min_temp = readings[0][0]
    max_hum = min_hum = readings[0][1]

    # find max and min
    for temp, hum in readings:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp
        if hum > max_hum:
            max_hum = hum
        if hum < min_hum:
            min_hum = hum

    return max_temp, min_temp, max_hum, min_hum


def get_average(readings):
    total_temp, total_hum = 0, 0
    # add all values
    for temp, hum in readings:
        total_temp += temp
        total_hum += hum
    # find average
    avg_temp = total_temp // len(readings)
    avg_hum = total_hum / len(readings)
    return round(avg_temp, 2), round(avg_hum, 2)


def get_exceeding_readings(readings, T, H):
    exceeded = []
    # check values greater than threshold
    for temp, hum in readings:
        if temp > T or hum > H:
            exceeded.append((temp, hum))
    return exceeded


# Read the input
n = int(input())
readings = []

# take input values
for i in range(n):
    t, h = map(int, input().split())
    readings.append((t, h))

# take threshold
T = int(input())
H = int(input())

# calling functions
max_temp, min_temp, max_hum, min_hum = get_max_min(readings)
avg_temp, avg_hum = get_average(readings)
exceeded = get_exceeding_readings(readings, T, H)

# print outputs
print("Maximum temperature:", max_temp)
print("Minimum temperature:", min_temp)
print("Maximum humidity:", max_hum)
print("Minimum humidity:", min_hum)
print("Average temperature:", avg_temp)
print("Average humidity:", avg_hum)
print("Hourly readings exceeding threshold:")
for temp, hum in exceeded:
    print(f"Temperature: {temp}, Humidity: {hum}")
