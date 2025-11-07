



import pygame
import random # for random position
from config.settings import (
    WIDTH,
    HEIGHT,
    POWERUP_SIZE,
    POWERUP_COLOR,
    POWERUP_DURATION,
    FREEZE_TIME,
)



# A class to represent a power-up item
class Powerup:
    def __init__(self):
        self.size = POWERUP_SIZE # size of the power-up set to powerup_size from settings
        self.color = POWERUP_COLOR # color of the power-up set to powerup_color from settings
        self.active = False # track if power-up is active
        self.start_time = 0 # track when power-up was activated
        self.reset() # initialize position and speed
        
        
    # A function to reset the power-up position
    def reset(self):
        """ Reset power-up position to the top with random x coordinate"""
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(-300, -100) # start above the screen
        self.speed = random.randint(3,6) # random fall speed starting from 3 to 6
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.effect = random.choice(["freeze_time", "slow_fall"]) # randomly choose a power-up effect
        self.active = False # reset active state
        
    def move(self):
        """ Move the power-up down the screen """
        self.rect.y += self.speed
        
        # reset position if it goes off the screen
        # then if the power-up goes off the screen, reset its position
        if self.rect.top > HEIGHT:
            self.reset()
    
    def activate(self):
        """ Activate the power-up effect """
        self.actice = True
        self.start_time = pygame.time.get_ticks() # record activation time
        
    
    def is_expired(self):
        if self.active:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= POWERUP_DURATION:
                self.active = False
                return True
        return False
        
    def draw(self, screen):
        """ Draw the power-up on the screen """
        pygame.draw.rect(screen, self.color, self.rect)