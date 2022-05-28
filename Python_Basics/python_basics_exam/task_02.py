# AND Processors
import math

processor_count = int(input())
worker_count = int(input())
work_days = int(input())

processor_cycle_time = 3  # the time for which a processor is made
processor_cost = 110.10  # the cost for which a processor is made
total_working_hours = worker_count * work_days * 8  # the total hours available for production

production_capacity = total_working_hours / processor_cycle_time
total_produce = math.floor(production_capacity)

planned_revenue = processor_count * processor_cost
achieved_revenue = total_produce * processor_cost

diff = abs(planned_revenue - achieved_revenue)

if total_produce < processor_count:
    print(f'Losses: -> {diff:.02f} BGN')
elif total_produce > processor_count:
    print(f'Profit: -> {diff:.02f} BGN')
else:
    print(f'Profit: -> {diff:.02f} BGN')