import numpy as np


class Bicycle():
    def __init__(self):
        # State Variables
        self.x = 0  # the x position of the rear wheel
        self.y = 0  # the y position of the rear wheel
        self.theta = 0  # the orientation angle of the bicycle frame
        self.delta = 0  # the front wheel steering angle
        self.beta = 0  # the orientation angle at the center of gravity of the frame due to side slip

        # Constant Properties
        self.L = 2  # the distance between the wheel centers
        self.lr = 1.2  # the distance from back wheel to center of gravity

        # Model constraints
        self.w_max = 1.22  # the maximum rotational speed of the bicycle
        self.delta_time = 0.01  # the sample time of simulation

    def reset(self):
        self.x = 0
        self.y = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0

    def step(self, v, w):
        if  w > self.w_max:
            w = self.w_max
        else:
            self.x = self.x + ((v * np.cos(self.theta + self.beta)) * self.delta_time)
            self.y = self.y + ((v * np.sin(self.theta + self.beta)) * self.delta_time)
            self.theta = self.theta + ((v * np.cos(self.beta) * np.tan(self.delta)) / self.L * self.delta_time)
            self.delta = self.delta + (w * self.delta_time)
            self.beta = np.arctan((self.lr * np.tan(self.delta)) / self.L)
        pass
