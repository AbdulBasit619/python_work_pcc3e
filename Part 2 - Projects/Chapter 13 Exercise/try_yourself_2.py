import sys

import pygame

from rain_settings import Settings
from raindrop import Drop


class Rain:
    """Overall class to manage rain using grid."""

    def __init__(self):
        """Initialize the grid, and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Rain")

        # Make a group of raindrops
        self.raindrops = pygame.sprite.Group()
        self._create_rain()

    def fall(self):
        """Class to make rain fall."""

        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_raindrops(self):
        """Update position of raindrops, get rid of old drops and generate new drops."""
        # Update the position of rain drop
        self.raindrops.update()

        screen_rect = self.screen.get_rect()
        # Remove drops that have reached the bottom
        for drop in self.raindrops.copy():
            if drop.rect.top > screen_rect.bottom:
                # Track the bottom most row that disappears off the screen
                # At the same time, create a new row that will fall from the top
                # This is achieved by resetting the top position of drop from bottom of screen to top
                drop.rect.top = 0
                drop.y = drop.rect.y

    def _create_rain(self):
        """Create rain."""

        # Create a raindrop and keep adding until there is no room left
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size
        # Save drop size for later (row/column calculations)
        self.drop_width = drop_width
        self.drop_height = drop_height

        current_x, current_y = drop_width, drop_height

        while current_y < self.settings.screen_height:

            while current_x < (self.settings.screen_width - 1 * drop_width):
                self._create_drop(current_x, current_y)
                current_x += 2 * drop_width

            # Finished a row, reset x value, increment y value
            current_x = drop_width
            current_y += 2 * drop_height

    def _create_drop(self, x_position, y_position):
        """Create a drop."""
        new_drop = Drop(self)
        new_drop.x = x_position
        new_drop.y = y_position
        new_drop.rect.x = x_position
        new_drop.rect.y = y_position
        self.raindrops.add(new_drop)

    def _update_screen(self):
        """Set and update the screen"""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    rain = Rain()
    rain.fall()
