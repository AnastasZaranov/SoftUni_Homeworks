total_student = 0
total_standard = 0
total_kid = 0

while True:
    student = 0
    standard = 0
    kid = 0
    seat_count = 0
    movie_name = input()
    if movie_name == "Finish":
        break
    else:
        for seat in range(seats):  # assign ticket_type for each available seat, unless "End".
            ticket_type = input()
            movie_occupancy = student + standard + kid
            seat_count += 1
            if seat_count == seats:
                elif ticket_type == "End":
                    print(f'{movie_name} - {(movie_occupancy / seats) * 100:.02f}% full.')
                    break
                elif ticket_type == "student":
                    student += 1
                    total_student += 1
                elif ticket_type == "standard":
                    standard += 1
                    total_standard += 1
                elif ticket_type == "kid":
                    kid += 1
                    total_kid += 1
            elif ticket_type == "End":
                print(f'{movie_name} - {(movie_occupancy / seats) * 100:.02f}% full.')
                break
            elif ticket_type == "student":
                student += 1
                total_student += 1
            elif ticket_type == "standard":
                standard += 1
                total_standard += 1
            elif ticket_type == "kid":
                kid += 1
                total_kid += 1
