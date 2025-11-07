# button.py
# Defines a reusable Button class for interactive menus.

import pygame
from config.settings import WHITE, GRAY, BLACK, FONT_NAME


class Button:
    def __init__(self, text, x, y, width, height, color_idle, color_hover):
        """Initialize button properties and appearance."""
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color_idle = color_idle
        self.color_hover = color_hover
        self.color = color_idle
        self.font = pygame.font.SysFont(FONT_NAME, 40)
        self.text_color = WHITE

    def draw(self, screen):
        """Draw the button with hover and text rendering."""
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color = self.color_hover
        else:
            self.color = self.color_idle

        pygame.draw.rect(screen, self.color, self.rect, border_radius=12)
        pygame.draw.rect(screen, BLACK, self.rect, 3, border_radius=12)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        """Check if the button was clicked."""
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            pygame.time.delay(150)  # small delay to prevent double-clicks
            return True
        return False