"""
Hauptspiel-Klasse mit Game Loop und Wirtschaftssystem.
"""

import pygame
from config import Config
from game_state import GameState


class Game:
    """Hauptspiel-Klasse."""
    
    def __init__(self, config=None):
        if config is None:
            config = Config()
        
        self.config = config
        self.game_state = GameState(config)
        
        # Pygame initialisieren
        pygame.init()
        
        # Bildschirm erstellen
        flags = 0
        if config.fullscreen:
            flags = pygame.FULLSCREEN
        
        self.screen = pygame.display.set_mode(
            (config.screen_width, config.screen_height),
            flags
        )
        pygame.display.set_caption("Confoederatio Helvetica")
        
        # Clock für FPS-Begrenzung
        self.clock = pygame.time.Clock()
        
        # Running-Flag
        self.running = True
        
        # Städte initialisieren (Schweizer Kontext)
        self._init_cities()
    
    def _init_cities(self):
        """Schweizer Handelsstädte initialisieren."""
        cities_data = [
            {"name": "Zürich", "x": 400, "y": 300},
            {"name": "Basel", "x": 200, "y": 150},
            {"name": "Genf", "x": 150, "y": 400},
            {"name": "Bern", "x": 300, "y": 250},
            {"name": "Luzern", "x": 350, "y": 280},
        ]
        
        for city_data in cities_data:
            city = {
                "name": city_data["name"],
                "x": city_data["x"],
                "y": city_data["y"],
                "supply": {},
                "demand": {},
                "prices": {}
            }
            
            # Güter für diese Stadt initialisieren
            goods = ["Getreide", "Wein", "Käse", "Wolle", "Eisen", "Silber"]
            for good in goods:
                import random
                city["supply"][good] = random.randint(50, 200)
                city["demand"][good] = random.randint(30, 150)
            
            self.game_state.cities.append(city)
    
    def run(self):
        """Hauptspiel-Schleife."""
        while self.running:
            # Events verarbeiten
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            
            # Spielzustand aktualisieren
            self.update()
            
            # Bildschirm zeichnen
            self.draw()
            
            # FPS begrenzen
            self.clock.tick(60)
        
        pygame.quit()
    
    def update(self):
        """Spielzustand aktualisieren."""
        pass
    
    def draw(self):
        """Bildschirm zeichnen."""
        self.screen.fill((30, 30, 50))
        
        # Titel anzeigen
        font = pygame.font.Font(None, 48)
        title_text = font.render("Confoederatio Helvetica", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.config.screen_width // 2, 50))
        self.screen.blit(title_text, title_rect)
        
        # Spielerinformationen anzeigen
        info_font = pygame.font.Font(None, 24)
        year_text = info_font.render(f"Jahr: {self.game_state.current_year}", True, (200, 200, 200))
        self.screen.blit(year_text, (20, 100))
        
        cash_text = info_font.render(f"Geld: {self.game_state.player.cash:.2f} Gulden", True, (200, 200, 200))
        self.screen.blit(cash_text, (20, 130))
        
        # Städte auf der Karte anzeigen
        for city in self.game_state.cities:
            # Stadtmarker zeichnen
            pygame.draw.circle(self.screen, (255, 200, 100), (city["x"], city["y"]), 8)
            
            # Stadtname anzeigen
            name_font = pygame.font.Font(None, 18)
            name_text = name_font.render(city["name"], True, (255, 255, 255))
            self.screen.blit(name_text, (city["x"] + 10, city["y"] - 10))
        
        pygame.display.flip()