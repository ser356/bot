
import numpy as np
import matplotlib.pyplot as plt
import random

def sierpinski(n):
    """ Genera los puntos del triángulo de Sierpinski. """
    if n == 0:
        return np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    else:
        prev_points = sierpinski(n - 1)
        top = (prev_points + np.array([0.5, np.sqrt(3)/2])) / 2
        left = (prev_points + np.array([0, 0])) / 2
        right = (prev_points + np.array([1, 0])) / 2
        return np.concatenate([left, top, right])
def random_color():
    idx = random.randint(0, 2)
    color = [0, 0, 0]
    color[idx] = random.choice([random.uniform(0, 0.3), random.uniform(0.7, 1)])
    color[(idx+1)%3] = random.random()
    color[(idx+2)%3] = random.random()
    return tuple(color)


def plot_sierpinski(n):
    """ Dibuja el triángulo de Sierpinski de nivel n. """
    points = sierpinski(n)
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.set_facecolor('black')
    for i in range(len(points)):
        plt.fill(points[i:i+2, 0], points[i:i+2, 1], color=random_color())
    plt.axis('equal')
    plt.axis('off')
    plt.savefig("sierpinski.png")