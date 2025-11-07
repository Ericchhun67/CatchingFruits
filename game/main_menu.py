
# main_menu.py
# Displays the start screen with buttons for Play and Quit.

import pygame
from config.settings import WIDTH, HEIGHT, TITLE, BG_COLOR, FONT_NAME, WHITE, FONT_NAME
from utils.button import Button
from utils.draw_text import draw_text


class MainMenu:
    def __init__(self, screen):
        """Initialize the main menu with buttons and layout."""
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_NAME, 64)
        self.title_text = TITLE

        # Define button dimensions and positions
        button_width, button_height = 220, 80
        center_x = WIDTH // 2 - button_width // 2
        self.play_button = Button("Play", center_x, HEIGHT // 2 - 60, button_width, button_height, (0, 200, 0), (0, 255, 0))
        self.quit_button = Button("Quit", center_x, HEIGHT // 2 + 60, button_width, button_height, (200, 0, 0), (255, 0, 0))
    
    
    # A method to add a background image to the main menu
    def add_background(self):
        bg_image = pygame.image.load("Catch_objects/assets/images/menu_bg.png")
        
    def run(self):
        """Display the menu and handle button clicks."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill(BG_COLOR)
            draw_text(self.screen, self.title_text, WIDTH // 2, HEIGHT // 4, center=True, font_size=72)

            # Draw buttons
            self.play_button.draw(self.screen)
            self.quit_button.draw(self.screen)

            # Check for clicks
            if self.play_button.is_clicked():
                return "start"
            if self.quit_button.is_clicked():
                return "quit"

            pygame.display.update()