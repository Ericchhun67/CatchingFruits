# timer.py
# Handles the main game countdown and freeze-time behavior for power-ups.

import pygame
from config.settings import GAME_DURATION


class Timer:
    def __init__(self, duration=GAME_DURATION):
        """Initialize the timer with the total game duration (in seconds)."""
        self.duration = duration
        self.start_time = pygame.time.get_ticks()
        self.time_left = duration
        self.paused = False
        self.pause_start = 0
        self.freeze_offset = 0  # Tracks total time frozen

    def update(self):
        """Update the timer every frame unless it's paused or frozen."""
        if not self.paused:
            elapsed_time = (pygame.time.get_ticks() - self.start_time - self.freeze_offset) / 1000
            self.time_left = max(0, self.duration - elapsed_time)

    def freeze(self, duration_ms):
        """
        Freeze the timer for a given duration (in milliseconds).
        Used by power-ups to stop time temporarily.
        """
        self.paused = True
        self.pause_start = pygame.time.get_ticks()
        self.freeze_offset += duration_ms

    def unfreeze(self):
        """Unfreeze the timer once the freeze period ends."""
        self.paused = False

    def reset(self):
        """Reset the timer back to its original duration."""
        self.start_time = pygame.time.get_ticks()
        self.time_left = self.duration
        self.paused = False
        self.freeze_offset = 0