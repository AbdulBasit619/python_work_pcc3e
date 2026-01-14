import sys

import pygame
from pygame.sprite import Sprite


class SidewaysRocket(Sprite):
    """A class to manage the sideways rocket's attributes and behaviour."""

    def __init__(self, game):
        """Initialize the rocket to set its position in the game."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load the rocket image and get its rect
        self.image = pygame.image.load("rocket_tilted.bmp")
        self.rect = self.image.get_rect()

        self.center_rocket()

        # Store the float for the rocket's exact vertical position
        self.y = float(self.rect.y)

        # Movement flags, start with the rocket that is not moving
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position vertically based on the movement flag."""

        # Update the rocket's y value, not the rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Update the rect object
        self.rect.y = self.y

    def center_rocket(self):
        """Center the rocket at the leftmost edge of the screen."""
        # Start the rocket at the middle left of the screen
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)
