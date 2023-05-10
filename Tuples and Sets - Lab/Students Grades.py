n = int(input())

student_grades = {}

for i in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name in student_grades:
        student_grades[name].append(grade)
    else:
        student_grades[name] = [grade]

for name, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    grades_str = ' '.join(f'{g:.2f}' for g in grades)
    print(f"{name} -> {grades_str} (avg: {avg_grade:.2f})")