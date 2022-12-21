import numpy as np
import matplotlib.pyplot as plt


class MathForm:
    def line(self):
        # y = kx + b линейная

        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        # polynomial fit with degree = 3
        model = np.poly1d(np.polyfit(x, y, 1))

        # add fitted polynomial line to scatterplot
        polyline = np.linspace(1, 3, 50)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline))
        plt.show()
        print(model)
    ###### ax^2 + bx + c квадратичная
    def square(self):
        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        # polynomial fit with degree = 3
        model = np.poly1d(np.polyfit(x, y, 2))

        # add fitted polynomial line to scatterplot
        polyline = np.linspace(1, 3, 50)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline))
        plt.show()
        print(model)

    # y=ax^3+bx^2+cx+d
    def cube(self):
        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        # polynomial fit with degree = 3
        model = np.poly1d(np.polyfit(x, y, 3))

        # add fitted polynomial line to scatterplot
        polyline = np.linspace(1, 3, 50)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline))
        plt.show()
        print(model)

    # y = a * x^b степенная
    # def degree(self, n):
    #     x = [0.9, 1, 11.1, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
    #     y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
    #     if n == None:
    #         n = 3

    # y = e^a + bx экспоненциальная
    def expon(self):
        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        model = np.poly1d(np.polyfit(x, np.log(y), 1))
        polyline = np.linspace(1, 3, 10)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline)+2)
        plt.show()
        print(model)

    def logr(self):
        x = [0.9, 1, 1.11, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        model = np.poly1d(np.polyfit(np.log(x), y, 1))
        polyline = np.linspace(1, 3, 10)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline) + 2)
        plt.show()
        print(model)