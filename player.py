



import pygame
from config.settings import PLAYER_SPEED, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR, WIDTH, HEIGHT



class player:
    def __init__(self):
        # start from the bottom center of the screen
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 30
        self.color = PLAYER_COLOR
        self.speed = PLAYER_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.score = 0 # track number of caught objects
    
    def handle_input(self, keys):
        """ Handle the player movement based on key inputs"""
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
    
    def draw(self, screen):
        """ Draw the player on the screen"""
        pygame.draw.rect(screen, self.color, self.rect)
        
    def check_collision(self, obj_group):
        """ Check for collisions with falling objects """
        collided_objects = [ obj for obj in obj_group if self.rect.colliderect(obj.rect)]
        return collided_objects
    
    def reset(self):
        """ Reset player position and score ( used for restaring the game)"""
        self.rect.x = WIDTH // 2 - self.width // 2
        self.rect.y = HEIGHT - self.height - 30
        self.score = 0