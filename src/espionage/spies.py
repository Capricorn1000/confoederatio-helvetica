"""
Spionagesystem - Spione anstellen und Missionen verwalten.
"""

import random


class Spy:
    """Ein Spion."""
    
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level  # 1-10
        self.target = None
        self.evidence_collected = []
    
    def assign_target(self, rival):
        """Spion auf Rivalen ansetzen."""
        self.target = rival
    
    def collect_evidence(self, game_round):
        """Beweise sammeln (pro Spielrunde)."""
        if not self.target:
            return None
        
        # Chance auf Beweissammlung basierend auf Skill-Level
        chance = self.skill_level * 0.1
        if random.random() < chance:
            evidence_type = random.choice(["bookkeeping", "tax_evasion", "contract_breach"])
            evidence = {"type": evidence_type, "quality": random.randint(1, 5)}
            self.evidence_collected.append(evidence)
            return evidence
        
        # Risiko entdeckt zu werden
        discovery_chance = (10 - self.skill_level) * 0.02
        if random.random() < discovery_chance:
            return "discovered"
        
        return None
    
    def get_evidence_value(self):
        """Gesamtwert der gesammelten Beweise."""
        total = 0
        for evidence in self.evidence_collected:
            total += evidence["quality"] * 10
        return total