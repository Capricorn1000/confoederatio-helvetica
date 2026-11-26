"""
Schlachtensystem - Gefechte zwischen Truppen.
"""

import random


class Battle:
    """Einzelne Schlacht."""
    
    def __init__(self, attacker, defender, location):
        self.attacker = attacker
        self.defender = defender
        self.location = location
        self.turns = 0
    
    def resolve_turn(self):
        """Eine Kampfrunde auflösen."""
        self.turns += 1
        
        # Angreifer attackiert
        attacker_damage = self.calculate_damage(self.attacker)
        self.defender.health -= attacker_damage
        
        if self.defender.health <= 0:
            return "attacker_wins"
        
        # Verteidiger kontert
        defender_damage = self.calculate_damage(self.defender)
        self.attacker.health -= defender_damage
        
        if self.attacker.health <= 0:
            return "defender_wins"
        
        return "ongoing"
    
    def calculate_damage(self, side):
        """Schaden einer Seite berechnen."""
        base_damage = side.troops * side.weapon_factor
        morale_factor = side.morale / 100.0
        
        # Zufallsfaktor für Realismus
        random_factor = random.uniform(0.8, 1.2)
        
        return int(base_damage * morale_factor * random_factor)