import math

standing_record, distance, meters_per_second = float(input()), float(input()), float(input())
water_resistance_time_accrual = math.floor((distance / 15) * 12.5)

contender_time = meters_per_second * distance + water_resistance_time_accrual

if contender_time > standing_record:
    print(f'No, he failed! He was {contender_time - standing_record:.02f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {contender_time:.02f} seconds.')

