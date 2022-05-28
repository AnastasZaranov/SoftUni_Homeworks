jury = int(input())
students_grades_sum = 0
presentation_count = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break

    presentation_count += 1
    current_student_score = 0
    for i in range(jury):
        score = float(input())
        students_grades_sum += score
        current_student_score += score
    print(f'{presentation} - {current_student_score/jury:.2f}.')

print(f"Student's final assessment is {students_grades_sum/(presentation_count * jury):.2f}.")
