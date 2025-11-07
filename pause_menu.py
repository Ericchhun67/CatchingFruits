# pause_menu.py
# Displays the pause screen and handles resume or quit actions.

import pygame
from config.settings import WIDTH, HEIGHT, BG_COLOR, FONT_NAME, WHITE
from utils.button import Button
from utils.draw_text import draw_text


class PauseMenu:
    def __init__(self, screen):
        """Initialize pause menu with buttons and text layout."""
        self.screen = screen
        button_width, button_height = 220, 80
        center_x = WIDTH // 2 - button_width // 2
        center_y = HEIGHT // 2 - button_height // 2

        # Buttons for resume and quit
        self.resume_button = Button("Resume", center_x, center_y - 80, button_width, button_height, (0, 150, 255), (0, 200, 255))
        self.quit_button = Button("Main Menu", center_x, center_y + 80, button_width, button_height, (255, 100, 100), (255, 0, 0))

    def run(self):
        """Display the pause menu and wait for user input."""
        paused = True

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill(BG_COLOR)
            draw_text(self.screen, "Game Paused", WIDTH // 2, HEIGHT // 4, center=True, font_name=FONT_NAME, font_size=72)

            self.resume_button.draw(self.screen)
            self.quit_button.draw(self.screen)

            if self.resume_button.is_clicked():
                return "resume"
            if self.quit_button.is_clicked():
                return "quit"

            # Also allow keyboard shortcut
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p] or keys[pygame.K_ESCAPE]:
                return "resume"

            pygame.display.update()