# 
# main.py
# 


import pygame
import sys

from config.settings import WIDTH, HEIGHT, FPS, TITLE, BG_COLOR
success, failure = pygame.init()
print(f"init:{success}, failed: {failure}")

from game.player import player
from game.object import FallingObject
from game.powerup import Powerup
from game.game_manager import GameManager
from game.timer import Timer

# Import menu and screen modules
from game.main_menu import MainMenu
from game.pause_menu import PauseMenu
from game.game_over import GameOver

# Import utility helpers
from utils.button import Button
from utils.draw_text import draw_text


# handle game errors during initializations
try:
    # set the game screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # set the game title
    pygame.display.set_caption(TITLE)
    # set game icon
    game_icon = pygame.image.load("Catch_objects/assets/icon/icon_basket.png")
    pygame.display.set_icon(game_icon)
    clock = pygame.time.Clock()
except Exception as e:
    # display an error message to the console
    print("Error initializing pygame:", e)
    # quit the game and exit
    sys.exit()



def game_background():
    """ Fill the screen with background image"""
    bg_image = pygame.image.load("Catch_objects/assets/images/bg_background.png")
    screen.blit(bg_image, (0, 0))




def main():
 
        
    # initialize states
    state_main_menu = "main_menu"
    state_playing = "playing"
    state_paused = "paused"
    state_game_over = "game_over"
    state = state_main_menu
    
    
    # initialize game manager
    game_manager = GameManager(screen)
    main_menu = MainMenu(screen)
    pause_menu = PauseMenu(screen)
    game_over = GameOver(screen)
    
    running = True # main game loop flag set to true to start the loop
    
    # main game loop as long as running is set to true
    while running:
        # handle quiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        
        # state machine
        if state == state_main_menu: # check if in main menu state
            # display start menu
            next_state = main_menu.run() # run main menu and get next state
            if next_state == "start": # if start game selected
                game_manager.reset() # reset game manager
                state = state_playing # change state to playing
            elif next_state == "quit":
                running = False
        # check if in playing state      
        elif state == state_playing: 
            # run core gameplay loop
            next_state = game_manager.run()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p] or keys[pygame.K_ESCAPE]:
                pause_menu = PauseMenu(screen)
                result = pause_menu.run()
                if result == "resume":
                    continue # go back to playing the game
                elif result == "quit":
                    state = state_main_menu
                    continue
            # check for state transitions
            if next_state == "pause":
                # change state to paused
                state = state_paused
            # check for game over
            elif next_state == "game_over":
                # change state to game over
                state = state_game_over
        # check if in paused state
        elif state == state_paused:
            # display pause menu
            next_state = pause_menu.run()
            # if resume selected, change state to playing
            if next_state == "resume":
                state = state_playing
            # else if quit selected, change state to main menu
            elif next_state == "quit":
                state = state_main_menu
        # check if in game over state
        elif state == state_game_over:
            # display game over screen
            next_state = game_over.run()
            # if restart selected, reset game and change state to playing
            if next_state == "restart":
                game_manager.reset() # reset game manager 
                state = state_playing
            elif next_state == "menu":
                state = state_main_menu
        # update the display and tick the clock
        pygame.display.update()
        clock.tick(FPS)
            
# run the main function if this file is executed directly   
if __name__ == "__main__":
    main()