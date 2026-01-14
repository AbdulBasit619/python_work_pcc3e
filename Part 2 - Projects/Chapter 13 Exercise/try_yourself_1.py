import sys
from random import randint

import pygame
import pygame.sprite

from star_grid_settings import Settings
from star import Star


class Grid:
    """A class to manage star grid."""

    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Star Grid")

        self.grid = pygame.sprite.Group()

    def run_game(self):
        # Create the grid once before the main loop
        self._make_grid()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_screen()
            self.clock.tick(60)

    def _make_grid(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x, current_y = star_width, star_height

        # Use screen_height for y and screen_width for x
        while current_y < (self.settings.screen_height - star_height):
            while current_x < (self.settings.screen_width - star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width
            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        new_star = Star(self)

        # Set the max jitter value of xy-coordinates
        max_jitter_x = int(new_star.rect.width * self.settings.star_jitter_factor)
        max_jitter_y = int(new_star.rect.height * self.settings.star_jitter_factor)

        # Calculate the random offset values of xy-coordinates
        jitter_x = randint(-max_jitter_x, max_jitter_x) if max_jitter_x > 0 else 0
        jitter_y = randint(-max_jitter_y, max_jitter_y) if max_jitter_y > 0 else 0

        new_x = x_position + jitter_x
        new_y = y_position + jitter_y

        max_x = self.settings.screen_width - new_star.rect.width
        max_y = self.settings.screen_height - new_star.rect.height

        new_x = max(0, min(new_x, max_x))
        new_y = max(0, min(new_y, max_y))

        new_star.x = float(new_x)
        new_star.rect.x = new_star.x

        new_star.y = float(new_y)
        new_star.rect.y = new_star.y

        self.grid.add(new_star)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # Draw all stars in the group
        self.grid.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    grid = Grid()
    grid.run_game()
