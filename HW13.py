def fun2(k: float, s='') -> str:
    if k == 0:
        return ''
    else:
        return '+ (' + str(k) + ')'


def equation(x1: float, x2: float, x3: float) -> None:
    A = -(x1 + x2 + x3)
    B = x1 * x2 + x1 * x3 + x2 * x3
    C = -(x1 * x2 * x3)

    print('- - - - - - - ')
    print('1-й вид уравнения: ', end='')
    print(f'(x-({str(x1)})) (x-({str(x2)})) (x-({str(x3)})) = 0')

    print('2-й вид уравнения: ', end='')
    print(f'x^3 {fun2(A)} * x^2 {fun2(B)} * x {fun2(C)} = 0')


print("Введите корни кубического уравнения ")
ROOT_A = float(input("1-й корень: "))
ROOT_B = float(input("2-й корень: "))
ROOT_C = float(input("3-й корень: "))

equation(ROOT_A, ROOT_B, ROOT_C)

#  (x-(0.5))(x-(-1.2))(x-(1))=0
#  x^3+(-3.0)*x^2+(3.0)*x+(-1.0)=0