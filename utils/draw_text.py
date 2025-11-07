# draw_text.py
# Helper function for drawing text to the screen easily and consistently.

import pygame
from config.settings import WHITE, FONT_NAME


def draw_text(
    screen,
    text,
    x,
    y,
    font_size=36,
    color=WHITE,
    center=False,
    font_name=FONT_NAME,
):
    """
    Draw text on the screen at a given position.
    
    Parameters:
    - screen: The surface to draw the text on.
    - text: The string to display.
    - x, y: Coordinates for text placement.
    - font_size: Size of the font (default: 36).
    - color: Text color (default: white).
    - center: If True, centers text around (x, y).
    - font_name: Font family (default: FONT_NAME from settings).
    """
    font = pygame.font.SysFont(font_name, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)

    screen.blit(text_surface, text_rect)