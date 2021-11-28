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

    print('Неизвестная операция')
    return None


print(calculation(input("Введите 1-е число:"),
      input("Введите 2-е число:"), input("Введите операцию (+, -, *, /):")))
