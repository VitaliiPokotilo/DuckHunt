# duck.py

import pygame
import random
from game_files.settings import WIDTH, HEIGHT

class Duck:
    def __init__(self, image, x, y, speed_x, speed_y):
        self.image = image
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def fly(self, current_speed_factor):
        self.x += self.speed_x * current_speed_factor
        self.y += self.speed_y

        if self.y <= 0 or self.y >= HEIGHT - 200:
            self.speed_y *= -1

        if self.x + 75 < 0 or self.x > WIDTH:
            self.x = WIDTH if self.x + 75 < 0 else -50
            self.y = random.randint(0, HEIGHT - 200)
            self.speed_y = random.choice([-2, 2])
