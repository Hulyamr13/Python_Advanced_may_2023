from project2.person import Person
from project2.employee import Employee
from project2.teacher import Teacher


person = Person()
print(person.sleep())


employee = Employee()
print(employee.get_fired())


teacher = Teacher()
print(teacher.sleep())
print(teacher.get_fired())
print(teacher.teach())
