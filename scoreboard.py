import pygame

class Scoreboard:
    """ A class to report scoring information. """
    def __init__(self, ai_game):
        """ Initialize scoring attributes. """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image.
        self.prep_score()
        
        
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
        
        
    def show_score(self): 
        """ Draw score to the screen. """
        self.screen.blit(self.score_image, self.score_rect) # Draw score image at location that score.rect specifies.       