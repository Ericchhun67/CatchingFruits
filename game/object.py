




import pygame
import random
from config.settings import WIDTH, HEIGHT, OBJECT_COLOR,OBJECT_SPEED_START, OBJECT_SIZE


class FallingObject:
    def __init__(self):
        self.size = OBJECT_SIZE
        self.color = OBJECT_COLOR
        self.reset()
    
    def reset(self):
        """ Reset object position to the top with random x coordinate"""
        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(-150, -50) # start above the screen
        self.speed = random.randint(OBJECT_SPEED_START, OBJECT_SPEED_START + 3)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
    
    
    
    def move(self):
        print(f"Before moving: y={self.rect.y}, speed={self.speed}")
        """ Move the object down the screen """
        self.rect.y += self.speed
        print(f"Afer moving: y={self.rect.y}")
        
        # if the object goes off the screen, reset its position
        if self.rect.top > HEIGHT:
            self.reset()
    
    def draw(self, screen):
        """ Draw the object on the screen"""
        pygame.draw.rect(screen, self.color, self.rect)
        # print(f"Drawing object at x={self.rect.x}, y={self.rect.y}")
        