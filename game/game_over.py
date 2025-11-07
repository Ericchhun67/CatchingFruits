# game_over.py
# Displays the Game Over screen and allows the player to restart or return to the main menu.

import pygame
from config.settings import WIDTH, HEIGHT, BG_COLOR, FONT_NAME, WHITE
from utils.button import Button
from utils.draw_text import draw_text


class GameOver:
    def __init__(self, screen):
        """Initialize Game Over screen with restart and menu buttons."""
        self.screen = screen
        button_width, button_height = 220, 80
        center_x = WIDTH // 2 - button_width // 2
        center_y = HEIGHT // 2 - button_height // 2

        self.restart_button = Button("Restart", center_x, center_y - 80, button_width, button_height, (0, 200, 0), (0, 255, 0))
        self.menu_button = Button("Main Menu", center_x, center_y + 80, button_width, button_height, (255, 100, 100), (255, 0, 0))

    def run(self, final_score):
        """Display the Game Over screen and handle button clicks."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill(BG_COLOR)

            # Draw main text
            draw_text(self.screen, "GAME OVER", WIDTH // 2, HEIGHT // 4, center=True, font_name=FONT_NAME, font_size=80)
            draw_text(self.screen, f"Final Score: {final_score}", WIDTH // 2, HEIGHT // 2 - 150, center=True, font_name=FONT_NAME, font_size=48)

            # Draw buttons
            self.restart_button.draw(self.screen)
            self.menu_button.draw(self.screen)

            # Handle clicks
            if self.restart_button.is_clicked():
                return "restart"
            if self.menu_button.is_clicked():
                return "menu"

            pygame.display.update()