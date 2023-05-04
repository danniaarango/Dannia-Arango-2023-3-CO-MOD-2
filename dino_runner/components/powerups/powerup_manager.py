import pygame
import random

from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE

class PowerupManager:
    def __init__(self):
        self.powerups = []
        self.duration = random.randint(3, 5)
        self.appears_shield_when = random.randint(30, 60)
        self.appears_hammer_when = random.randint(80, 110)

    def update(self, game):
        #controlamos las apariciones
        if len(self.powerups) == 0 and self.appears_shield_when == game.score.count:
            self.generate_powerup()
        #animacion de powerup
        for powerup in self.powerups:
            powerup.update(game.game_speed, self.powerups)
            #colision del dino con el powerup y desaparece
            if game.player.dino_rect.colliderect(powerup.rect):
                self.powerups.remove(powerup)

                powerup.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = SHIELD_TYPE 
                game.player.power_up_time = powerup.start_time + (self.duration * 1000)
        #controlamos las apariciones
        if len(self.powerups) == 0 and self.appears_hammer_when == game.score.count:
            self.generate_powerup()
        #animacion de powerup
        for powerup in self.powerups:
            powerup.update(game.game_speed, self.powerups)
            #colision del dino con el powerup y desaparece
            if game.player.dino_rect.colliderect(powerup.rect):
                self.powerups.remove(powerup)

                powerup.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = HAMMER_TYPE
                #game.player.power_up_time = powerup.start_time + (self.duration * 1000)

    def draw(self, screen):
        for powerup in self.powerups:
            powerup.draw(screen)

    def reset_powerups(self):
        self.powerups = []
        self.appears_shield_when = random.randint(70, 90)
        self.appears_hammer_when = random.randint(100, 10)

    def generate_powerup(self):
        self.appears_shield_when = random.randint(250, 300)
        powerup = Shield()
        self.powerups.append(powerup)
        self.appears_hammer_when = random.randint(250, 300)
        powerup = Hammer()
        self.powerups.append(powerup)