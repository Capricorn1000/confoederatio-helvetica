"""
KI-General-Steuerung - Computer übernimmt Führung der Truppen.
"""

import random


class AI_General:
    """Computer-gesteuerter General."""
    
    def __init__(self, difficulty="medium"):
        self.difficulty = difficulty  # easy, medium, hard
    
    def make_decision(self, battle_state):
        """Entscheidung für nächste Aktion treffen."""
        if battle_state.attacker.health < battle_state.defender.health * 0.5:
            return "retreat"
        
        if battle_state.turns > 10 and self.difficulty == "easy":
            return "negotiate"
        
        # Standard: Weiterkämpfen
        return "fight"
    
    def choose_tactics(self, situation):
        """Taktik basierend auf Situation wählen."""
        if situation == "defensive":
            return "hold_position"
        elif situation == "offensive":
            return "advance"
        else:
            return random.choice(["hold_position", "advance"])