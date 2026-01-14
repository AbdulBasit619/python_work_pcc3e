import sys

import pygame

from settings import Settings
from character import Character


class Game:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Practice Game")

        self.character = Character(self)

    def run_game(self):
        """Start the main loop for the game."""
        # Respond to key presses and mouse movements
        while True:
            self._manage_events()
            self._update_screen()
            self.clock.tick(60)

    def _manage_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance
    game = Game()
    game.run_game()
