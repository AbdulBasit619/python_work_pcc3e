import sys
from time import sleep
from pathlib import Path

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from sound import SoundEffects


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.sound = SoundEffects(self)

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # Create an instance and import file contents
        # to store game statistics,
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.path = Path("highscore.txt")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # Make the play button and center it.
        self.play_button = Button(self, "Play")

        # Make difficulty selector buttons.
        self._make_difficulty_buttons()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.path.write_text(str(self.stats.high_score))
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_difficulty_buttons(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.path.write_text(str(self.stats.high_score))
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player wants to Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active and self._difficulty_selected():
            # Reset the game statistics
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.settings._initialize_dynamic_settings()
            self.game_active = True

            # Get rid of any bullets or aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create an empty fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _difficulty_selected(self):
        return self.easy.selected or self.medium.selected or self.hard.selected

    def _fire_bullet(self):
        """Create a new bullet, add it to the bullets group and play sound."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.sound.play_shoot()

    def _create_fleet(self):
        """Create the fleet of aliens."""

        # Create an alien and keep adding aliens until there is no room left.
        # Spacing between the aliens is one alien width and one a line height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 20 * alien_height):
            while current_x < (self.settings.screen_width - 4 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, increment y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        can_play = self._difficulty_selected()

        if not self.game_active:
            self.play_button.draw_button(enabled=can_play)
            self.easy.draw_button()
            self.medium.draw_button()
            self.hard.draw_button()

        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of the bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided
        # and play sound.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sound.play_alien_hit()
            self.sb.prep_score()
            self.sb.check_high_scores()

        if not self.aliens:
            self._start_new_level()

    def _start_new_level(self):
        """Start a new level when all the aliens on the screen have been destroyed."""
        # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level
        self.stats.level += 1
        self.sb.prep_level()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _ship_hit(self):
        """Respond to a ship being hit by an alien."""

        if self.stats.ships_left > 0:
            # Play the sound when ship is hit.
            self.sound.play_ship_hit()

            # Decrement ships_left and update the scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_score()
            self.sb.prep_high_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Get rid of any bullets or aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ships.
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Respond to an alien hitting the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _make_difficulty_buttons(self):
        """Make three different buttons for difficulty: easy, medium, hard."""
        self.easy = Button(self, "Easy")
        self.medium = Button(self, "Medium")
        self.hard = Button(self, "Hard")

        # Vertical spacing.
        gap_x = 50
        gap_y = 80

        # Play button already centered.
        play_centerx, play_centery = self.play_button.rect.center

        # Move difficulty button below play
        y_pos = play_centery + gap_y

        self.medium.rect.center = (play_centerx, y_pos)
        self.easy.rect.center = (play_centerx - self.medium.width - gap_x, y_pos)
        self.hard.rect.center = (play_centerx + self.medium.width + gap_x, y_pos)

        # Update text positions
        for btn in (self.easy, self.medium, self.hard):
            btn.msg_image_rect.center = btn.rect.center

    def _check_difficulty_buttons(self, mouse_pos):
        """Handle difficulty selection."""
        if self.easy.rect.collidepoint(mouse_pos):
            self._set_difficulty("easy")
        elif self.medium.rect.collidepoint(mouse_pos):
            self._set_difficulty("medium")
        elif self.hard.rect.collidepoint(mouse_pos):
            self._set_difficulty("hard")

    def _set_difficulty(self, level):
        """Set difficulty and highlight selected buttons."""
        self.easy.selected = False
        self.medium.selected = False
        self.hard.selected = False

        if level == "easy":
            self.easy.selected = True
            self.settings.set_easy()
        elif level == "medium":
            self.medium.selected = True
            self.settings.set_medium()
        elif level == "hard":
            self.hard.selected = True
            self.settings.set_hard()


if __name__ == "__main__":
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
