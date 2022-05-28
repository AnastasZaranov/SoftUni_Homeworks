# 01. Moon
import math

average_speed = float(input())
fuel_consumption = float(input())  # per 100 km distance
moon_stay = 3
round_trip = 384400 * 2

total_round_trip_time = moon_stay + round_trip / average_speed
print(f'{math.ceil(total_round_trip_time)}')

total_fuel_consumption = (round_trip / 100) * fuel_consumption
print(f'{math.ceil(total_fuel_consumption)}')



