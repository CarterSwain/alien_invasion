import sys
from time import sleep

import pygame 

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien_1 import Alien
from star import Star

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """ Initialize game, and create game resources. """
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        
        self._create_fleet()
        self._create_star_field()
        
        # Start Alien Invasion in an active state.
        
    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()       
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """ Respond to key presses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """ Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()         
            
    def _check_keyup_events(self, event):
        """ Respond to key releases """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group. """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)         
    
    def _update_bullets(self):
        """ Update position of bullets and get rid of old bullets. """
        # Update bullet position
        self.bullets.update()
            
        # Get rid of old bullets.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collision()
            
    def _check_bullet_alien_collision(self):
        """ Respond to bullet-alien collisions """
        # Remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(
                 self.bullets, self.aliens, False, True) # If no longer wanting a bullet that deletes anything in path, change first boolean arg to 'True' to delete bullet)
        
        if not self.aliens:
            # Destroying existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            
    def _ship_hit(self):
        """ Respond to the ship being hit by an alien. """
        # Decrement ships_left.
        self.stats.ships_left -= 1
        
        # Get rid of any remaining bullets or aliens.
        self.bullets.empty()
        self.aliens.empty()
        
        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()
        
        # Pause.
        sleep(0.5)         
            
    def _update_aliens(self):
        """ Check if the fleet is at an edge, then update positions. """
        self._check_fleet_edges()
        self.aliens.update()  
        
        # Look for alien-ship collisions. 
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()      
    
    def _create_fleet(self):
        """ Create the fleet of aliens. """
        # Create alien and keep adding aliens until there is no more room left.
        # Space between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        # Determine number of aliens per row
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)
    
        # Determine number of rows
        available_space_y = self.settings.screen_height - 3 * alien_height
        number_rows = available_space_y // (2 * alien_height)

        # Create rows of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                x_position = alien_width + 2 * alien_width * alien_number
                y_position = alien_height + 2 * alien_height * row_number
                self._create_alien(x_position, y_position)
                   
    def _create_alien(self, x_position, y_position):
        """ Create an alien and place it in the fleet. """
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
    def _check_fleet_edges(self):
        """ Respond appropriately if any aliens have reached an edge. """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """ Drop entire fleet and change direction. """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1   
        
    def _check_aliens_bottom(self):
        """ Check if aliens have reached the bottom of the screen. """
        for alien in self.alien.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship was hit.
                self._ship_hit()
                break                 
        
    def _create_star_field(self):
        """ Create a field of randomly positioned stars. """
        for _ in range(250):  
           star = Star(self)
           self.stars.add(star)
                           
    def _update_screen(self):
        """ Update images on the screen and flip to the new screen. """
        self.screen.fill(self.settings.bg_color)
        
        # Draw stars.
        self.stars.draw(self.screen)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
                           
        pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()            
