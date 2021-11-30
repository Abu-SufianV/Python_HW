"""
Домашнее задание 21

Для заданной математической функции y=f(x) разработать программу построения графика функции на интервале от 3,
1 до 6. На графике предусмотреть наличие заголовка и подзаголовка, осей, подписей осей и линий сетки.

Построить график функции sin(1/(3*x))*exp(x)
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(3.1, 6, 100)
y = np.sin(1 / 3 ** x) * np.exp(x)

plt.title("Построение графика функции на интервале от 3,1 до 6")
plt.suptitle("Зависимость Y = sin(1/(3*x))*exp(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()

plt.plot(x, y)
plt.show()
