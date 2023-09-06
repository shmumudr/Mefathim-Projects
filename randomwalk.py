import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class RandomWalk:

    def __init__(self, step, dimensions):
        self.step = step
        self.dim = dimensions
        self.coordinates = [[0 for step in range(self.step)] for dim in range(self.dim)]

    def walk(self):
        for step in range(self.step - 1):
            random_dim = random.randint(0, self.dim - 1)
            for dim in range(self.dim):
                if dim == random_dim:
                    self.move(dim, step)
                else:
                    self.stay_put(dim, step)

    def move(self, dim, step):
        direction = 1
        flip = random.random()
        if flip < 0.5:
            direction = -1
        self.coordinates[dim][step + 1] = self.coordinates[dim][step] + direction

    def stay_put(self, dim, step):
        self.coordinates[dim][step + 1] = self.coordinates[dim][step]

    def display(self):
        x, y, z = self.coordinates
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z)
        plt.plot(x, y, z)
        plt.show()


r = RandomWalk(30, 3)
r.walk()
r.display()


