def perform_calculation(input_string):
    parts = input_string.split()
    number1 = float(parts[0])
    sign = parts[1]
    number2 = int(parts[2])

    if sign == '/':
        result = number1 / number2
    elif sign == '*':
        result = number1 * number2
    elif sign == '-':
        result = number1 - number2
    elif sign == '+':
        result = number1 + number2
    elif sign == '^':
        result = number1 ** number2

    formatted_result = format(result, '.2f')
    return formatted_result