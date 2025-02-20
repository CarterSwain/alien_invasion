import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """ A class to manage the group of stars. """
    
    def __init__(self, ai_game):
        """ Initialize single star at random position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the image, resize it, and get its rect.
        self.image = pygame.image.load('images/blue_star.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        
        # Randomize star position within screen dimensions
        self.rect.x = randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = randint(0, self.settings.screen_height - self.rect.height)
        
       