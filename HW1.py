# Задание №1

def calculation(x, y, operation):
    x = int(x)
    y = int(y)
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    else:
        print('Неизвестная операция')
        return None


print(calculation(input(), input(), input()))
