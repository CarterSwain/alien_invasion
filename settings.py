class Settings:
    """ A class to store all settings for Alien Invasion. """
    
    def __init__(self):
        """ Initialize game's static settings. """
        
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (63, 17, 115)
        
        # Ship settings.
        self.ship_limit = 3
        
        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (1, 255, 78)
        self.bullets_allowed = 7
        
        # Alien settings.
        self.fleet_drop_speed = 5
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        # Default difficulty setting (Default to medium)
        self.difficulty = "medium"
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game. """
        if self.difficulty == "easy":
            self.ship_speed = 1.5
            self.bullet_speed = 2.0
            self.alien_speed = 0.8
        elif self.difficulty == "medium":
            self.ship_speed = 1.7
            self.bullet_speed = 2.5
            self.alien_speed = 1.1
        elif self.difficulty == "hard":
            self.ship_speed = 1.5
            self.bullet_speed = 3.5
            self.alien_speed = 1.5    
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Scoring settings.
        self.alien_points = 50
        
    def set_difficulty(self, difficulty):
        """ Set game difficulty and reinitialize dynamic settings. """
        self.difficulty = difficulty
        self.initialize_dynamic_settings()
        
        
    def increase_speed(self):
        """ Increase speed settings. """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale        
    
        
        