import pygame

class Alien:
    """ A class to manage the Alien. """
    
    def __init__(self, ai_game):
        """ Initialize Alien and get its starting position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the Alien and get its rect.
        self.image = pygame.image.load('images/alien_invasion_alien1.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new Alien at the Middle Top of the screen.
        self.rect.midtop = self.screen_rect.midtop
        
    def blitme(self):
        """ Draw the alien at its current location. """
        self.screen.blit(self.image, self.rect)
            
        
        