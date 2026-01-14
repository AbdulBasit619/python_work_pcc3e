import pygame

from pygame.sprite import Sprite


class Drop(Sprite):
    """A class to create and manage a raindrop."""

    def __init__(self, rain):
        """Initialize the rain drop and set its target position."""
        super().__init__()
        self.screen = rain.screen
        self.settings = rain.settings

        # Load the image and set its rect attribute
        self.image = pygame.image.load("raindrop.bmp")
        self.rect = self.image.get_rect()

        # Place each new drop at the top-left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store raindrop's exact position as floats for smooth movement
        self.rect.x = float(self.rect.x)
        self.rect.y = float(self.rect.y)

    def check_edges(self):
        """Check if the rain drop falls below the bottom edge of the screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom

    def update(self):
        """Make a drop fall."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
