# Exercise Nr. 8: On time for exam
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
exam_count = exam_hour * 60 + exam_minute
arrival_count = arrival_hour * 60 + arrival_minute
remainder = 0
remainder_hour = 0
remainder_minute = 0

if exam_count > arrival_count:
    remainder = exam_count - arrival_count
    if remainder <= 1:
        print(f'On time')
    if 2 <= remainder <= 30:
        print(f'On time\n{remainder} minutes before the start')
    if 31 <= remainder <= 59:
        print(f'Early\n{remainder} minutes before the start')
    if remainder >= 60:
        remainder_hour = remainder // 60
        remainder_minute = remainder % 60
        print(f'Early\n{remainder_hour}:{remainder_minute:02d} hours before the start')
if exam_count == arrival_count:
    print('On time')
if exam_count < arrival_count:
    remainder = arrival_count - exam_count
    if remainder <= 59:
        print(f'Late\n{remainder:02d} minutes after the start')
    if remainder >= 60:
        remainder_hour = remainder // 60
        remainder_minute = remainder % 60
        print(f'Late\n{remainder_hour}:{remainder_minute:02d} hours after the start')
