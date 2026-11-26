"""
Hauptspiel-Klasse mit Game Loop und Wirtschaftssystem.

Integriert Spionagesystem und Rechtssystem (Kapitel 2).
"""

import pygame
from config import Config
from game_state import GameState, Rival
from economy.trade import buy_good, sell_good


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
        
        # Nachrichtensystem
        self.message = ""
        self.message_timer = 0
        
        # Städte initialisieren (Schweizer Kontext)
        self._init_cities()
    
    def _init_cities(self):
        """Schweizer Handelsstädte initialisieren."""
        import random
        
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
                city["supply"][good] = random.randint(50, 200)
                city["demand"][good] = random.randint(30, 150)
            
            self.game_state.cities.append(city)
    
    def set_message(self, msg):
        """Nachricht anzeigen."""
        self.message = msg
        self.message_timer = 180  # 3 Sekunden bei 60 FPS
    
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
                    elif event.key == pygame.K_1:
                        # Handel in Zürich
                        self._trade_in_city(0)
                    elif event.key == pygame.K_2:
                        # Handel in Basel
                        self._trade_in_city(1)
                    elif event.key == pygame.K_3:
                        # Handel in Genf
                        self._trade_in_city(2)
                    elif event.key == pygame.K_s:
                        # Spion anstellen
                        self._hire_spy()
                    elif event.key == pygame.K_a:
                        # Spionage-Mission starten
                        self._start_espionage_mission()
                    elif event.key == pygame.K_l:
                        # Prozess einreichen
                        self._file_court_case()
            
            # Spielzustand aktualisieren
            self.update()
            
            # Bildschirm zeichnen
            self.draw()
            
            # FPS begrenzen
            self.clock.tick(60)
        
        pygame.quit()
    
    def _trade_in_city(self, city_index):
        """Handel in einer Stadt durchführen."""
        if city_index >= len(self.game_state.cities):
            return
        
        city = self.game_state.cities[city_index]
        
        # Einfacher Testhandel: Kaufe Getreide, verkaufe es sofort
        buy_success, buy_msg = buy_good(
            self.game_state.player, 
            city, 
            "Getreide", 
            10, 
            5.0
        )
        
        if buy_success:
            sell_success, sell_msg = sell_good(
                self.game_state.player,
                city,
                "Getreide",
                10,
                7.0
            )
            
            if sell_success:
                self.set_message(f"{buy_msg}\n{sell_msg}")
    
    def _hire_spy(self):
        """Einen Spion anstellen."""
        from espionage.spies import hire_spy
        
        spy, cost = hire_spy(self.game_state.player)
        
        if spy:
            self.set_message(f"Spion {spy.name} (Skill {spy.skill_level}) für {cost} Gulden angestellt.")
        else:
            self.set_message(cost)  # Fehlermeldung
    
    def _start_espionage_mission(self):
        """Eine Spionage-Mission starten."""
        if not self.game_state.player.spies:
            self.set_message("Keine Spione verfügbar. Stelle zuerst einen Spion an (Taste S).")
            return
        
        if not self.game_state.rivals:
            self.set_message("Keine Rivalen zum Überwachen.")
            return
        
        # Ersten verfügbaren Spion auf ersten Rivalen ansetzen
        spy = self.game_state.player.spies[0]
        rival = self.game_state.rivals[0]
        
        spy.assign_target(rival)
        self.set_message(f"Spion {spy.name} überwacht jetzt {rival.name}.")
    
    def _file_court_case(self):
        """Ein Gerichtsverfahren einreichen."""
        if not self.game_state.player.spies:
            self.set_message("Keine Beweise gesammelt. Starte zuerst eine Spionage-Mission.")
            return
        
        # Prüfen ob genug Beweise vorhanden sind
        total_evidence_value = 0
        for spy in self.game_state.player.spies:
            total_evidence_value += spy.get_evidence_value()
        
        from espionage.evidence import can_file_lawsuit, get_lawsuit_threshold
        
        if not can_file_lawsuit(total_evidence_value):
            threshold = get_lawsuit_threshold()
            self.set_message(f"Nicht genug Beweise für einen Prozess. Benötigt {threshold} Punkte, hat {total_evidence_value}.")
            return
        
        # Prozess gegen ersten Rivalen einreichen
        rival = self.game_state.rivals[0]
        
        court_case = self.game_state.file_court_case(
            self.game_state.player,
            rival,
            "trade_dispute"
        )
        
        # Beweise dem Fall hinzufügen
        for spy in self.game_state.player.spies:
            for evidence in spy.evidence_collected:
                court_case.add_evidence("plaintiff", evidence)
        
        self.set_message(f"Prozess gegen {rival.name} eingereicht (Fall #{court_case.id}).")
    
    def update(self):
        """Spielzustand aktualisieren."""
        if self.message_timer > 0:
            self.message_timer -= 1
    
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
        
        # Spione anzeigen
        if self.game_state.player.spies:
            spy_count = len(self.game_state.player.spies)
            spy_text = info_font.render(f"Spione: {spy_count}", True, (200, 200, 200))
            self.screen.blit(spy_text, (20, 160))
        
        # Gerichtsverfahren anzeigen
        if self.game_state.active_court_cases:
            case_count = len(self.game_state.active_court_cases)
            case_text = info_font.render(f"Gerichtsverfahren: {case_count}", True, (255, 200, 100))
            self.screen.blit(case_text, (20, 190))
        
        # Inventar anzeigen
        if self.game_state.player.goods:
            inv_text = info_font.render(f"Inventar: {self.game_state.player.goods}", True, (200, 200, 200))
            self.screen.blit(inv_text, (20, 220))
        
        # Nachricht anzeigen
        if self.message_timer > 0:
            msg_font = pygame.font.Font(None, 20)
            lines = self.message.split("\n")
            for i, line in enumerate(lines):
                msg_text = msg_font.render(line, True, (100, 255, 100))
                self.screen.blit(msg_text, (20, 260 + i * 25))
        
        # Städte auf der Karte anzeigen
        for i, city in enumerate(self.game_state.cities):
            # Stadtmarker zeichnen
            pygame.draw.circle(self.screen, (255, 200, 100), (city["x"], city["y"]), 8)
            
            # Stadtname anzeigen
            name_font = pygame.font.Font(None, 18)
            name_text = name_font.render(city["name"], True, (255, 255, 255))
            self.screen.blit(name_text, (city["x"] + 10, city["y"] - 10))
            
            # Tastaturkürzel anzeigen
            key_font = pygame.font.Font(None, 14)
            key_text = key_font.render(f"[{i+1}]", True, (150, 150, 150))
            self.screen.blit(key_text, (city["x"] - 15, city["y"] + 10))
        
        # Anleitung anzeigen
        help_font = pygame.font.Font(None, 16)
        help_lines = [
            "Drücke 1-3 für Handel in den Städten",
            "S: Spion anstellen | A: Spionage-Mission starten",
            "L: Prozess einreichen (bei ausreichender Beweislage)"
        ]
        
        for i, line in enumerate(help_lines):
            help_text = help_font.render(line, True, (150, 150, 150))
            self.screen.blit(help_text, (20, self.config.screen_height - 60 + i * 20))
        
        pygame.display.flip()