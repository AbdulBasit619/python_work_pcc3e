import pygame


class Character:
    """A class to manage the character"""

    def __init__(self, game):
        """Initialize the character and set its target position."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the character image and get its rect
        self.image = pygame.image.load("images/character.bmp")
        self.rect = self.image.get_rect()

        # Place the character at the middle of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
