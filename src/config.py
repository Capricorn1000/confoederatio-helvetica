"""
Konfiguration und Optionen für Confoederatio Helvetica.
"""


class Config:
    """Spielkonfiguration."""
    
    def __init__(self):
        # Spieloptionen
        self.game_duration_until_1800 = False  # Spieldauer bis 1800 erweiterbar
        self.bribery_enabled = True  # Gerichtsbestechung ein-/ausschaltbar
        self.historical_events_enabled = True  # Historische Ereignisse ein-/ausschalten
        self.adventures_enabled = True  # Abenteuer/Sub-Plots ein-/ausschalten
        self.random_events_enabled = True  # Zufallsmeldungen ("Schicksal") aktivieren
        self.help_tips_enabled = True  # Hilfen von erfahrenen Kaufleuten
        
        # Grafikoptionen
        self.screen_width = 1024
        self.screen_height = 768
        self.fullscreen = False
        self.color_mode = "32bit"  # "256color" or "32bit"
        
        # Soundoptionen
        self.sound_enabled = True
        self.music_enabled = True
        self.volume = 0.8
        
        # Spielgeschwindigkeit
        self.game_speed = 1.0
    
    def save(self, filepath="data/config.json"):
        """Konfiguration speichern."""
        import json
        config_dict = {
            "game_duration_until_1800": self.game_duration_until_1800,
            "bribery_enabled": self.bribery_enabled,
            "historical_events_enabled": self.historical_events_enabled,
            "adventures_enabled": self.adventures_enabled,
            "random_events_enabled": self.random_events_enabled,
            "help_tips_enabled": self.help_tips_enabled,
            "screen_width": self.screen_width,
            "screen_height": self.screen_height,
            "fullscreen": self.fullscreen,
            "color_mode": self.color_mode,
            "sound_enabled": self.sound_enabled,
            "music_enabled": self.music_enabled,
            "volume": self.volume,
            "game_speed": self.game_speed
        }
        
        with open(filepath, 'w') as f:
            json.dump(config_dict, f)
    
    def load(self, filepath="data/config.json"):
        """Konfiguration laden."""
        import json
        try:
            with open(filepath, 'r') as f:
                config_dict = json.load(f)
            
            self.game_duration_until_1800 = config_dict.get("game_duration_until_1800", False)
            self.bribery_enabled = config_dict.get("bribery_enabled", True)
            self.historical_events_enabled = config_dict.get("historical_events_enabled", True)
            self.adventures_enabled = config_dict.get("adventures_enabled", True)
            self.random_events_enabled = config_dict.get("random_events_enabled", True)
            self.help_tips_enabled = config_dict.get("help_tips_enabled", True)
            self.screen_width = config_dict.get("screen_width", 1024)
            self.screen_height = config_dict.get("screen_height", 768)
            self.fullscreen = config_dict.get("fullscreen", False)
            self.color_mode = config_dict.get("color_mode", "32bit")
            self.sound_enabled = config_dict.get("sound_enabled", True)
            self.music_enabled = config_dict.get("music_enabled", True)
            self.volume = config_dict.get("volume", 0.8)
            self.game_speed = config_dict.get("game_speed", 1.0)
        except FileNotFoundError:
            pass  # Use defaults if no config file exists