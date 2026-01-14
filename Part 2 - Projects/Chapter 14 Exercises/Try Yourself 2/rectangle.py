import pygame
from pygame.sprite import Sprite


class Rectangle(Sprite):
    """A class to create and manage rectangle."""

    def __init__(self, game):
        """Create a vertical rectangle at the right edge of the screen."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.rectangle_color

        # Create a rectangle rect at top right of the screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(
            0, 0, self.settings.rectangle_width, self.settings.rectangle_height
        )
        self.rect.topright = self.screen_rect.topright
        self.rect.x -= 30
        self.rect.y += 30

        # Store the rectangle's position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Move the rectangle up and down."""
        # Update the exact position of the rectangle
        self.y += self.settings.rectangle_speed * self.settings.rectangle_direction

        # Update the rect position
        self.rect.y = self.y

    def check_edges(self):
        """Return true if rectangle touches the edges."""
        return (self.rect.top <= 0) or (self.rect.bottom >= self.screen_rect.bottom)

    def draw_rectangle(self):
        """Draw rectangle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
