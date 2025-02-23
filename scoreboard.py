import pygame
from pygame.sprite import Group
from pathlib import Path
import json
from ship import Ship

class Scoreboard:
    """ A class to report scoring information. """
    def __init__(self, ai_game):
        """ Initialize scoring attributes. """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
        
    def prep_level(self):
        """ Turn the level into a rendered image. """
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)
        
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10 
        
        
    def prep_ships(self):
        """ Show how many ships are left. """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
           
        
    def prep_score(self):
        """ Turn the score into a rendered image. """
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color) # We pass the score_str to Render which creates image.
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 # Place score image's right edge 20 pixels from right edge of screen.
        self.score_rect.top = 20 # Place score image's top edge 20 pixels down from top of screen.
        
       
    def prep_high_score(self):
        """ Turn the high score into a rendered image. """
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)
        
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top 
        
        
    def check_high_score(self):
        """ Check to see if there is a new high score. """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            
            
    def save_high_score(self):
        """ Write high score to JSON file to be saved when player quits the game. """
        high_score = self.stats.high_score
        path = Path('high_score.json')
        contents = json.dumps(high_score)
        path.write_text(contents)
                           
     
    def read_high_score(self):
        """ IF there is a high score, read high score that was previously saved. """
        path = Path('high_score.json')
        if path.exists():
            try:
                contents = path.read_text()
                high_score = json.loads(contents)
                return high_score if isinstance(high_score, int) else 0
            except (json.JSONDecodeError, ValueError):
                return 0
        return 0
        
        
    def show_score(self): 
        """ Draw scores and level to the screen. """
        self.screen.blit(self.score_image, self.score_rect) # Draw score image at location that score.rect specifies.
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)       