"""
Spielzustands-Management für Confoederatio Helvetica.

Verwaltet den gesamten Spielzustand einschließlich Spieler, Städte, Rivalen,
Spione und Gerichtsverfahren.
"""


class Player:
    """Spieler-Daten."""
    
    def __init__(self, name="Spieler"):
        self.name = name
        self.cash = 10000.0  # Startkapital in Gulden
        self.goods = {}  # {good_name: quantity}
        self.trades = []  # Aktive Handelsgeschäfte
        self.spies = []  # Angestellte Spione
        self.troops = []  # Eigene Truppen
        self.reputation = 50  # Ruf (0-100)


class Rival:
    """Ein Handelsrival."""
    
    def __init__(self, name):
        import random
        self.name = name
        self.cash = random.randint(5000, 20000)
        self.reputation = random.randint(30, 80)


class GameState:
    """Gesamter Spielzustand."""
    
    def __init__(self, config):
        import random
        self.config = config
        self.current_year = 1500
        self.current_month = 1
        self.player = Player()
        self.cities = []  # Liste aller Städte
        self.rivals = []  # Liste der Rivalen
        self.active_events = []  # Aktive Ereignisse
        self.active_adventures = []  # Aktive Abenteuer/Sub-Plots
        self.game_over = False
        
        # Spionage & Rechtssystem (Kapitel 2)
        self.active_court_cases = []  # Laufende Gerichtsverfahren
        self.completed_court_cases = []  # Abgeschlossene Verfahren
        
        # Rivalen initialisieren
        self._init_rivals()
    
    def _init_rivals(self):
        """Handelsrivalen initialisieren."""
        rival_names = [
            "Hans Fugger",
            "Jakob Welser",
            "Heinrich Imhoff",
            "Bartholomäus Herlin"
        ]
        
        for name in rival_names:
            self.rivals.append(Rival(name))
    
    def advance_month(self):
        """Eine Spielmonat voranschreiten."""
        from espionage.spies import pay_spy_maintenance
        
        self.current_month += 1
        if self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
            
            # Jahresende-Verarbeitung
            self.process_year_end()
        
        # Spionage-Aktivitäten aktualisieren
        self._update_espionage()
    
    def _update_espionage(self):
        """Spionagemissionen für alle aktiven Spione aktualisieren."""
        for spy in self.player.spies:
            if spy.target:
                result = spy.collect_evidence(self.current_year * 12 + self.current_month)
                
                if result == "discovered":
                    # Spion entdeckt - Mission beendet
                    spy.target = None
                    return f"Spion {spy.name} wurde von {spy.target} entdeckt!"
    
    def process_year_end(self):
        """Jahresende-Verarbeitung (Zinsen, historische Ereignisse, etc.)."""
        from espionage.spies import pay_spy_maintenance
        
        # Spione bezahlen
        maintenance_cost = pay_spy_maintenance(self.player)
        
        # Historische Ereignisse für dieses Jahr prüfen
        pass
    
    def file_court_case(self, plaintiff, defendant, case_type="trade_dispute"):
        """Ein neues Gerichtsverfahren einreichen."""
        from legal.court import CourtCase
        
        court_case = CourtCase(plaintiff, defendant, case_type)
        self.active_court_cases.append(court_case)
        
        return court_case
    
    def resolve_court_case(self, court_case):
        """Ein Gerichtsverfahren abschließen und Urteil fällen."""
        verdict, details = court_case.calculate_verdict(
            bribery_enabled=self.config.bribery_enabled
        )
        
        self.active_court_cases.remove(court_case)
        self.completed_court_cases.append(court_case)
        
        return verdict, details
    
    def to_dict(self):
        """Spielzustand serialisieren."""
        return {
            "current_year": self.current_year,
            "current_month": self.current_month,
            "player_cash": self.player.cash,
            "game_over": self.game_over,
            "active_court_cases": len(self.active_court_cases)
        }
    
    @classmethod
    def from_dict(cls, state_dict, config):
        """Spielzustand deserialisieren."""
        game = cls(config)
        game.current_year = state_dict["current_year"]
        game.current_month = state_dict["current_month"]
        game.player.cash = state_dict["player_cash"]
        game.game_over = state_dict["game_over"]
        return game