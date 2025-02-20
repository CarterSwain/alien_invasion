import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single Alien in the fleet. """
    
    def __init__(self, ai_game):
        """ Initialize the Alien and set its starting position. """
        super().__init__()
        self.screen = ai_game.screen
        
        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien2.png')
        self.rect = self.image.get_rect()
        
        # Start each new Alien at the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)  
        
        