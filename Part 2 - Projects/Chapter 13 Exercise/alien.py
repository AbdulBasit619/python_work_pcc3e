import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in a fleet."""

    def __init__(self, game):
        """Initialize alien."""

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the alien and it's rect attribute
        self.image = pygame.image.load("alien_tilted.bmp")
        self.rect = self.image.get_rect()

        # Start the alien at the top right of screen.
        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.rect.x = float(self.rect.x)
        self.rect.y = float(self.rect.y)

    def _check_edges(self):
        """Return true if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)

    def update(self):
        """Move the alien up or down."""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y
