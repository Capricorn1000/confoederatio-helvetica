"""
Belagerungssystem - Festungsbelagerungen.
"""


class Siege:
    """Belagerung einer Stadt/Festung."""
    
    def __init__(self, attacker, defender_city):
        self.attacker = attacker
        self.defender_city = defender_city
        self.turns_elapsed = 0
        self.status = "ongoing"
    
    def advance_turn(self):
        """Belagerung eine Runde voranschreiten lassen."""
        self.turns_elapsed += 1
        
        # Verteidiger verliert allmählich an Stärke (Aushungerung)
        self.defender_city.supply -= 10
        
        if self.defender_city.supply <= 0:
            self.status = "attacker_wins"
        
        return self.status
    
    def surrender(self):
        """Verteidiger kapituliert."""
        self.status = "attacker_wins"