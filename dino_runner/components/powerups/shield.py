from dino_runner.components.powerups.powerup import Powerup
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE

class Shield(Powerup):
    def __init__(self): 
        self.start_time = 0
        super().__init__(SHIELD, SHIELD_TYPE)
        