import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets fired from rocket."""

    def __init__(self, game):
        """Create a buller object at the current rocket's position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and set position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        # Start the bullet at the rocket's right edge (nose)
        self.rect.midleft = game.rocket.rect.midright

        # Store the bullet's position as a float
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen"""
        # Update the exact position of the bullet
        self.x += self.settings.bullet_speed

        # Update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
