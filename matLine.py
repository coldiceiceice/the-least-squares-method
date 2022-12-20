import numpy as np
import matplotlib.pyplot as plt


class MathForm:
    def line(self):
        # y = kx + b
        N = 10  # число экспериментов
        sigma = 3  # стандартное отклонение наблюдаемых значений
        k = 1  # теоретическое значение параметра k
        b = 10  # теоретическое значение параметра b

        x = np.array(range(N))
        f = np.array([k * z + b for z in range(N)])
        y = f + np.random.normal(0, sigma, N)

        # вычисляем коэффициенты
        mx = x.sum() / N
        my = y.sum() / N
        a2 = np.dot(x.T, x) / N  #умножение X транспонированного на X
        a11 = np.dot(x.T, y) / N

        kk = (a11 - mx * my) / (a2 - mx ** 2) # вычисление оценок для К и B
        bb = my - kk * mx

        ff = np.array([kk * z + bb for z in range(N)]) # линейный график аппроксимации

        plt.scatter(x, y, s=2, c='red') # набор точек
        plt.plot(f)  # теореическая прямая
        plt.plot(ff, c='red') # эксперементальная прямая
        plt.grid(True)
        plt.show()


    ###### ax^2 + bx + c
    def square(self):
        def my_quadratic_function(x):
            return x ** 2 - 0.6 * x + 1

        xx = np.linspace(0, 1, 500)
        plt.plot(xx, my_quadratic_function(xx))
        plt.show()
