from collections import defaultdict

n = int(input())

student_grades = defaultdict(list)

for i in range(n):
    name, grade = input().split()
    grade = float(grade)
    student_grades[name].append(grade)

for name, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    grades_str = ' '.join(f'{g:.2f}' for g in grades)
    print(f"{name} -> {grades_str} (avg: {avg_grade:.2f})")