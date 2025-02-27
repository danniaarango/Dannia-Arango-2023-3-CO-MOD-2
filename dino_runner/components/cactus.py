import random
import pygame

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
    CACTUS = {
              "SMALL": (SMALL_CACTUS, 325),
              "LARGE": (LARGE_CACTUS, 300)
        }
    def __init__(self, cactus_type):
       image, cactus_pos = self.CACTUS[cactus_type]
       self.type = random.randint(0, 2)
       super().__init__(image, self.type)
       self.rect.y = cactus_pos

    def draw(self, screen):
        screen.blit(self.image[self.obstacle_type], (self.rect.x, self.rect.y))

class Cactus2(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 300
        
