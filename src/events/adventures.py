"""
Abenteuer/Sub-Plots - Über 30 \"Spiele im Spiel\" über mehrere Jahre hinweg.
"""


class Adventure:
    """Einzelnes Abenteuer/Sub-Plot."""
    
    def __init__(self, id, title, description, duration_years):
        self.id = id
        self.title = title
        self.description = description
        self.duration_years = duration_years
        self.current_year = 0
        self.completed = False
    
    def advance(self, game_state):
        """Abenteuer eine Runde voranschreiten lassen."""
        self.current_year += 1
        
        if self.current_year >= self.duration_years:
            self.complete(game_state)
    
    def complete(self, game_state):
        """Abenteuer abschließen und Belohnung geben."""
        self.completed = True
        # Belohnung oder Konsequenz anwenden
        pass


# Beispiel-Abenteuer (Schweizer Themen)
ADVENTURES = [
    Adventure(1, "Alpenhandel sichern", 
             "Verteidige die Handelsrouten über den Gotthardpass gegen Räuber.", 3),
    Adventure(2, "Bankgeheimnis etablieren", 
             "Baue das Schweizer Bankgeheimnis auf und ziehe internationale Kunden an.", 5),
    Adventure(3, "Söldnerkapitäne rekrutieren", 
             "Gewinne die besten Schweizer Söldner für deine eigenen Zwecke.", 2),
]