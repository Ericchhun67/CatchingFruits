# game_manager.py
# Controls game logic: collisions, score, timer, and power-up effects.

import pygame
import random
from config.settings import (
    WIDTH,
    HEIGHT,
    BG_COLOR,
    GAME_DURATION,
    SPAWN_INTERVAL,
    POWERUP_SPAWN_INTERVAL,
    FREEZE_TIME,
    FONT_NAME,
    SCORE_FONT_SIZE,
    TIMER_FONT_SIZE,

)

from game.player import player
from game.object import FallingObject
from game.powerup import Powerup
from game.timer import Timer
from utils.draw_text import draw_text


class GameManager:
    def __init__(self, screen):
        self.screen = screen # Pygame display surface
        self.player = player() # initialize player object
        self.objects = [FallingObject() for _ in range(5)] # start with 5 falling objects
        self.powerups = [] # Empty list to store power-ups
        self.timer = Timer(GAME_DURATION) # set timer and store in GamerTimer
        self.score = 0 # initialize score set to 0
        self.last_spawn_time = pygame.time.get_ticks() # Track last object spawn time
        self.last_powerup_spawn_time = pygame.time.get_ticks()
        self.freeze_active = False # Track if freeze power-up is active
        self.freeze_start = 0 # Track when freeze started and set to 0
    
    # A method to reset the game state
    def reset(self):
        # Reset player, objects, power-ups, score, and timer
        self.player.reset()
        # set objects to initial state and spawn 5 new ones using a list comprehension
        self.objects = [FallingObject() for _ in range(5)]
        # set power-ups to an empty list
        self.powerups = []
        # set score back to 0
        self.score = 0 
        # reset the timer
        self.timer.reset()
        # reset freeze state
        self.freeze_active = False
        
    # Method to spawn falling objects at intervals
    def spawn_objects(self):
        # get current time and see if enough time has passed since last spawn
        current_time = pygame.time.get_ticks()
        # check if enough time has passed since last spawn
        if current_time - self.last_powerup_spawn > POWERUP_SPAWN_INTERVAL:
            # spawn a new falling object and add to the list
            self.objects.append(FallingObject())
            # update last spawn time
            self.last_spawn_time = current_time
            
    # method to spawn power-ups at intervals
    def spawn_powerups(self):
        # get current time set to pygame time ticks 
        current_time = pygame.time.get_ticks()
        # check if enough time has passed since last power-up spawn
        if current_time - self.last_powerup_spawn > POWERUP_SPAWN_INTERVAL:
            # spawn a new power-up and add to the list
            self.objects.append(Powerup())
            self.last_powerup_spawn_time = current_time

    # method to update game state 
    def update(self):
        # handle player input keys 
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys) # move player based on input
        
        # Freeze time effect (stop objects from falling)
        if self.freeze_active:
            # check if freeze duration has passed - freeze_time 
            if pygame.time.get_ticks() - self.freeze_start > FREEZE_TIME:
                self.freeze_active = False # deactivate freeze effect set to false
        else: 
            # loop through objects and power-ups without moving them
            for obj in self.objects:
                print("moving objects....") # debug print
                obj.move()
            # loop through power-ups 
            for powerup in self.powerups:
                powerup.move()
        
        # handle collisions between player and falling objects
        caught_objects = self.player.check_collision(self.objects)
        # loop through caught objects and update score and reset objects positions
        for obj in caught_objects:
            self.score += 1 
            obj.reset()
        
        # handle collisions with power-ups
        caught_powerups = self.player.check_collision(self.powerups)
        # loop through caught power-ups and apply their effects
        for pwr in caught_powerups:
            # check the type of power-up and apply effect
            if pwr.effect == "freeze_time":
                self.freeze_active = True
                self.freeze_start = pygame.time.get_ticks()
            elif pwr.effect == "slow_fall":
                for obj in self.objects:
                    obj.speed = max(1, obj.speed // 2)
            pwr.reset()
        # timer countdown update
        if not self.freeze_active:
            self.timer.update()
        
        # check for game over(timer runs out)
        if self.timer.time_left <= 0:
            return "game_over"
        
        return "playing"
        
    def draw(self):
        self.screen.fill(BG_COLOR)
        self.player.draw(self.screen)
        for obj in self.objects:
            obj.draw(self.screen)
        for pwr in self.powerups:
            pwr.draw(self.screen)
            
       # Draw score and timer
        draw_text(
            self.screen,
            f"Score: {self.score}",
            25,
            20,
            font_name=FONT_NAME,
            font_size=SCORE_FONT_SIZE,
        )
        
        draw_text(
            self.screen,
            f"Timer: {self.timer.time_left/ 1000:.2f}",
            25,
            50,
            font_name=FONT_NAME,
            font_size=SCORE_FONT_SIZE,
)
        
    def run(self):
        print("running......")
        print(f"objects count: {len(self.objects)}")
        next_state = self.update()
        self.draw()
        return next_state
        


