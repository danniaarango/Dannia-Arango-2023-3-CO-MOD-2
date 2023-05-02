import pygame

from dino_runner.components.cactus import Cactus, Cactus2
from dino_runner.components.birds import Birds1, Birds2, Birds3
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self) :
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = Cactus2(LARGE_CACTUS)
            self.obstacles.append(cactus)

            cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)

            birds = Birds1(BIRD)
            self.obstacles.append(birds)
            birds = Birds2(BIRD)
            self.obstacles.append(birds)
            birds = Birds3(BIRD)
            self.obstacles.append(birds)

        for obstacle in self.obstacles :
            obstacle.update(game.game_speed, self.obstacles)
            pygame.time.delay(90)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
