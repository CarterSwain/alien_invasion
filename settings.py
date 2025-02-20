class Settings:
    """ A class to store all settings for Alien Invasion. """
    
    def __init__(self):
        """ Initialize game's settings. """
        
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (63, 17, 115)
        
        # Ship settings.
        self.ship_speed = 1.5
        
        # Bullet settings.
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (1, 255, 78)
        self.bullets_allowed = 3