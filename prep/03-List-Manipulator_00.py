def list_manipulator(*args):
    new_list = []

    numbers = args[0]
    first_command = args[1]
    second_command = args[2]


    if len(args) > 3:
        for el in args[3:]:
            new_list.append(el)


    if first_command == 'add' and second_command == 'beginning':
        new_list = new_list[::-1]
        for el in new_list:
            numbers.insert(0, el)

        return numbers


    elif first_command == 'add' and second_command == 'end':
        for el in new_list:
            numbers.append(el)

        return numbers


    elif first_command == 'remove' and second_command == 'beginning':
        if new_list:
            res = int(''.join(str(x) for x in new_list))                  #numbers = numbers[len(new_list)+1::]
            numbers = numbers[res::]

        else:
            numbers.pop(0)                                               # numbers = numbers[1::]

        return numbers


    elif first_command == 'remove' and second_command == 'end':
        if new_list:
            res = int(''.join(str(x) for x in new_list))                #numbers = numbers[:-len(new_list)-1]
            numbers = numbers[:-res:]
        else:
            numbers.pop()

        return numbers






print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

print(list_manipulator([1,2,3], "add", "beginning", 20), [20, 1, 2, 3])


import unittest

# class Tests(unittest.TestCase):
#     def test_zero(self):
#         self.assertEqual(list_manipulator([1,2,3], "remove", "end"), [1, 2])
#         self.assertEqual(list_manipulator([1,2,3], "remove", "beginning"), [2, 3])
#         self.assertEqual(list_manipulator([1,2,3], "add", "beginning", 20), [20, 1, 2, 3])
#         self.assertEqual(list_manipulator([1,2,3], "add", "end", 30), [1, 2, 3, 30])
#         self.assertEqual(list_manipulator([1,2,3], "remove", "end", 2), [1])
#         self.assertEqual(list_manipulator([1,2,3], "remove", "beginning", 2), [3])
#         self.assertEqual(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40), [20, 30, 40, 1, 2, 3])
#         self.assertEqual(list_manipulator([1,2,3], "add", "end", 30, 40, 50), [1, 2, 3, 30, 40, 50])
#
# if __name__ == "__main__":
#     unittest.main()