import os

def create_file(file_name):
    with open(file_name, 'w') as file:
        pass

def add_content(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content + '\n')

def replace_content(file_name, old_string, new_string):
    try:
        with open(file_name, 'r') as file:
            file_content = file.readlines()

        modified_content = []
        for line in file_content:
            modified_line = line.replace(old_string, new_string)
            modified_content.append(modified_line)

        with open(file_name, 'w') as file:
            file.write(''.join(modified_content))

    except FileNotFoundError:
        print("An error occurred")

def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


while True:
    command = input()

    if command == "End":
        break

    command_parts = command.split('-')

    if command_parts[0] == "Create":
        file_name = command_parts[1]
        create_file(file_name)

    elif command_parts[0] == "Add":
        file_name = command_parts[1]
        content = command_parts[2]
        add_content(file_name, content)

    elif command_parts[0] == "Replace":
        file_name = command_parts[1]
        old_string = command_parts[2]
        new_string = command_parts[3]
        replace_content(file_name, old_string, new_string)

    elif command_parts[0] == "Delete":
        file_name = command_parts[1]
        delete_file(file_name)
