import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle

class Birds1(Obstacle):
    def __init__(self, image):
        self.type = random.randint()
        super().__init__(image, self.type)
        self.rect.y = 260
      

class Birds2(Obstacle):
    def __init__(self, image):
        self.type = random.randint()
        super().__init__(image, self.type)
        self.rect.y = 220
        

class Birds3(Obstacle):
    def __init__(self, image):
        self.type = random.randint()
        super().__init__(image, self.type)
        self.rect.y = 170
        


        
        
        