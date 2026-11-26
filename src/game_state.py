"""
Spielzustands-Management für Confoederatio Helvetica.
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


class GameState:
    """Gesamter Spielzustand."""
    
    def __init__(self, config):
        self.config = config
        self.current_year = 1500
        self.current_month = 1
        self.player = Player()
        self.cities = []  # Liste aller Städte
        self.rivals = []  # Liste der Rivalen
        self.active_events = []  # Aktive Ereignisse
        self.active_adventures = []  # Aktive Abenteuer/Sub-Plots
        self.game_over = False
    
    def advance_month(self):
        """Eine Spielmonat voranschreiten."""
        self.current_month += 1
        if self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
            
            # Jahresende-Verarbeitung
            self.process_year_end()
    
    def process_year_end(self):
        """Jahresende-Verarbeitung (Zinsen, historische Ereignisse, etc.)."""
        # Zinsen auf Kredite berechnen
        pass
        
        # Historische Ereignisse für dieses Jahr prüfen
        pass
    
    def to_dict(self):
        """Spielzustand serialisieren."""
        return {
            "current_year": self.current_year,
            "current_month": self.current_month,
            "player_cash": self.player.cash,
            "game_over": self.game_over
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