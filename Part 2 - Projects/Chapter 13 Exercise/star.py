import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to create and manage a single star."""

    def __init__(self, grid):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = grid.screen

        # Load star image and set its rect attribute
        self.image = pygame.image.load("star.bmp")
        self.rect = self.image.get_rect()

        # Start each new star at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Keep floating-point x/y for more precise movement if needed
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
