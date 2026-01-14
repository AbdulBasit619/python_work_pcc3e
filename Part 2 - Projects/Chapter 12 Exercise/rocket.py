import pygame


class Rocket:
    """Class to manage the rocket's attributes and actions."""

    def __init__(self, game):
        """Initialize the rocket and set it's position."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load the rocket image and get it's rect
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()

        # Start the rocket at the middle of the screen
        self.rect.center = self.screen_rect.center

        # Store the float for the ship's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags, start with rocket that is not moving
        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
