import pygame
from pygame.sprite import Sprite


class Rocket(Sprite):
    """A class to manage the rocket."""

    def __init__(self, game):
        """Create a rocket and set it's position."""
        super().__init__()

        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the rocket and get it's rect.
        self.image = pygame.image.load("images/rocket_tilted.bmp")
        self.rect = self.image.get_rect()

        # Center the rocket.

        self.center_rocket()

        # Movement flag, start with a rocket that is not moving.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""

        # Update the rocket's y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Update the rect object.
        self.rect.y = self.y

    def center_rocket(self):
        """Center the rocket on the screen."""

        # Center the rocket at the center left of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store the float for the rocket's exact vertical position.
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw rocket at the current location."""
        self.screen.blit(self.image, self.rect)
