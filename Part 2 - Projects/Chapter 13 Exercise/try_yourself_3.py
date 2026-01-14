import sys
from time import sleep

import pygame
import pygame.sprite

from sideways_rocket import SidewaysRocket
from game_stats import GameStats
from sideways_rocket_settings import Settings
from sideways_bullet import Bullet
from alien import Alien


class SidewaysShooter:
    """Overall class to implement Sideways shooter game."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Sideways Shooter")

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.screen_rect = self.screen.get_rect()
        self.rocket = SidewaysRocket(self)

        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Start game in an active state.
        self.game_active = True

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._manage_events()
            if self.game_active:
                self.rocket.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _manage_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""

        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _update_aliens(self):
        """Check edges, and update aliens."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-rocket collisions.
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self._rocket_hit()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien._check_edges():
                self._change_fleet_direction()
                break

    def _rocket_hit(self):
        """Respond to a rocket being hit by an alien or vice-versa."""

        if self.stats.rockets_left > 0:
            # Decrement rockets left.
            self.stats.rockets_left -= 1

            # Get rid of any bullets or aliens.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the rocket.
            self._create_fleet()
            self.rocket.center_rocket()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False

    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Create the fleet of aliens."""

        # Create an alien and then keep adding aliens until there is no room left.
        # Spacing between the aliens is one alien width and one a line height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Start at the top right edge of screen.
        current_x = self.settings.screen_width - 2 * alien_width
        current_y = alien_height

        while current_x > 20 * alien_width:
            while current_y < (self.settings.screen_height - 2 * alien_height):
                self._create_alien(current_x, current_y)
                current_y += 2 * alien_height

            # Finished a column, reset y value, increment x value
            current_y = alien_height
            current_x -= 2 * alien_width

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in a row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.y = y_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    game = SidewaysShooter()
    game.run_game()
