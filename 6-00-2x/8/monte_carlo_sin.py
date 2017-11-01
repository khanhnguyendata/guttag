import random
import math
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')


def integrate_sin(start, end, points):
    """
    Find the value when integrating sin(x) between 2 values
    :param points: number of points to populate the area for the Monte Carlo simulation
    :param start: value where integration starts
    :param end: value where integration ends
    :return: result when integrating sin(x) between start and end
    """
    rectangle_area = end - start

    points_under_graph = 0

    x_inside_coordinates = []
    y_inside_coordinates = []
    x_outside_coordinates = []
    y_outside_coordinates = []

    for point in range(points):
        x = start + random.random() * (end - start)
        if math.sin(x) >= 0:
            y = random.random()
        else:
            y = -random.random()
        if abs(y) <= abs(math.sin(x)):
            points_under_graph += 1
            x_inside_coordinates.append(x)
            y_inside_coordinates.append(y)
        else:
            x_outside_coordinates.append(x)
            y_outside_coordinates.append(y)

    area_under_graph = (points_under_graph / points) * rectangle_area

    plt.figure()
    x = np.linspace(start, end, points)
    plt.plot(x, np.sin(x), '-', color='black')
    plt.plot(x_inside_coordinates, y_inside_coordinates, 'o', color='red')
    plt.plot(x_outside_coordinates, y_outside_coordinates, 'o', color='blue')
    plt.title(f'Integrating sin x between {start} and {end} with {points} points: {area_under_graph}')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.xlim(start, end)
    plt.show()


integrate_sin(0, math.pi*2, 10000)
