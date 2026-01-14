import sys

import pygame

from task_3_settings import Settings
from rectangle import Rectangle
from task_3_rocket import Rocket
from task_3_bullet import Bullet
from task_3_button import Button


class Game:
    """Overall class to manage the game."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        self.clock = pygame.time.Clock()
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Rectangle Shooter")

        # Make a rectangle instance.
        self.rectangle = Rectangle(self)

        # Make a rocket instance.
        self.rocket = Rocket(self)

        # Initialize a Bullet Group.
        self.bullets = pygame.sprite.Group()

        # Initialize Play button.
        self.play_button = Button(self, "Play")

        # Start game in an inactive state.
        self.game_active = False

        # Track missed bullets
        self.misses = 0
        self.max_misses = 3

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.rocket.update()
                self._update_bullets()
                self._update_rectangle()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Check for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
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

    def _check_play_button(self, mouse_pos):
        """Start a new game when a player clicks to Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        """Start a new game."""
        self.game_active = True
        self.settings._initialize_dynamic_settings()
        self.settings.rectangle_speed = 2.0

        # Get rid of any bullets and remove the rectangle.
        self.bullets.empty()
        self.rectangle.remove()

        # Create rectangle and center the rocket.
        self.rectangle.draw_rectangle()
        self.rocket.center_rocket()

        # Hide mouse cursor
        pygame.mouse.set_visible(False)

        # Reset misses.
        self.misses = 0

    def _update_rectangle(self):
        """Check edges, move and speed up the rectangle accordingly."""

        if self.rectangle.check_edges():
            self.settings.rectangle_direction *= -1
            if self.settings.rectangle_speed < self.settings.max_rectangle_speed:
                self.settings.rectangle_speed += self.settings.speedup_scale
        self.rectangle.update()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""

        # Update bullet position.
        self.bullets.update()

        # Get rid of bullets that have disappeared from the right edge of screen,
        # and increment the miss counter
        for bullet in self.bullets.copy():
            screen_rect = self.screen.get_rect()
            if bullet.rect.left >= screen_rect.right:
                self.bullets.remove(bullet)
                self.misses += 1

                # Check if game should end.
                if self.misses >= self.max_misses:
                    self._end_game()

        self._check_bullet_rectangle_collision()

    def _check_bullet_rectangle_collision(self):
        """Check collisions between bullet group and rectangle"""

        collision = pygame.sprite.spritecollide(self.rectangle, self.bullets, True)

        if collision:
            self.rectangle.draw_rectangle()

    def _end_game(self):
        """End the current game state."""
        self.game_active = False

        # Clear bullets.
        self.bullets.empty()

        # Reset the rectangle.
        self.rectangle = Rectangle(self)

        # Reset the rocket.
        self.rocket.center_rocket()

        # Show the mouse cursor.
        pygame.mouse.set_visible(True)

        # Reset miss counter
        self.misses = True

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        # Draw rocket on to the screen
        self.rocket.blitme()
        # Draw bullets to the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw rectangle on to the screen.
        self.rectangle.draw_rectangle()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
