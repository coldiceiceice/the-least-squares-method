import statistics

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
from scipy import stats


class MathForm:
    def line(self):
        # y = kx + b

        x = [0.9, 1, 11.1, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        # polynomial fit with degree = 3
        model = np.poly1d(np.polyfit(x, y, 1))

        # add fitted polynomial line to scatterplot
        polyline = np.linspace(1, 12, 50)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline))
        plt.show()
        print(model)
    ###### ax^2 + bx + c
    def square(self):
        x = [0.9, 1, 11.1, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        # polynomial fit with degree = 3
        model = np.poly1d(np.polyfit(x, y, 2))

        # add fitted polynomial line to scatterplot
        polyline = np.linspace(1, 12, 50)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline))
        plt.show()
        print(model)

    def cube(self):
        x = [0.9, 1, 11.1, 1.2, 1.24, 1.34, 1.4, 1.43, 1.5, 1.55]
        y = [4.08, 3.7875, 3.4594, 3.34125, 3.465, 3.104, 3.193, 3.1007, 3.06, 2.891]
        # polynomial fit with degree = 3
        model = np.poly1d(np.polyfit(x, y, 3))

        # add fitted polynomial line to scatterplot
        polyline = np.linspace(1, 12, 50)
        plt.scatter(x, y)
        plt.plot(polyline, model(polyline))
        plt.show()
        print(model)