"""
Spionagesystem - Spione anstellen und Missionen verwalten.

Spieler können Spione auf Rivalen ansetzen, Beweise sammeln und
strategische Vorteile erlangen. Basierend auf dem Fugger II System
mit Schweizer Kontext (Handels- und Bankspionage zwischen Kantonen).
"""

import random


# Kosten für Spione basierend auf Skill-Level
SPY_HIRE_COSTS = {
    1: 50,     # Anfänger
    2: 100,
    3: 175,
    4: 275,
    5: 400,    # Durchschnittlich
    6: 550,
    7: 750,
    8: 1000,   # Erfahren
    9: 1350,
    10: 1800   # Meister
}

# Monatliche Aufrechterhaltungskosten (20% der Anstellungskosten)
SPY_MAINTENANCE_FACTOR = 0.2


class Spy:
    """Ein Spion mit Skill-Level und aktiver Mission."""
    
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level  # 1-10
        self.target = None
        self.evidence_collected = []
        self.mission_rounds = 0
    
    @property
    def hire_cost(self):
        """Kosten für die Anstellung dieses Spions."""
        return SPY_HIRE_COSTS[self.skill_level]
    
    @property
    def maintenance_cost(self):
        """Monatliche Aufrechterhaltungskosten."""
        return int(self.hire_cost * SPY_MAINTENANCE_FACTOR)
    
    def assign_target(self, rival):
        """Spion auf Rivalen ansetzen."""
        self.target = rival
        self.mission_rounds = 0
    
    def collect_evidence(self, game_round):
        """Beweise sammeln (pro Spielrunde)."""
        if not self.target:
            return None
        
        self.mission_rounds += 1
        
        # Chance auf Beweissammlung basierend auf Skill-Level und Missiondauer
        base_chance = self.skill_level * 0.08
        duration_bonus = min(self.mission_rounds * 0.02, 0.2)  # Max +20% nach 10 Runden
        chance = base_chance + duration_bonus
        
        if random.random() < chance:
            evidence_type = self._select_evidence_type()
            quality = self._determine_quality()
            evidence = {
                "type": evidence_type,
                "quality": quality,
                "collected_by": self.name,
                "round": game_round
            }
            self.evidence_collected.append(evidence)
            return evidence
        
        # Risiko entdeckt zu werden (höher bei weniger fähigen Spionen)
        discovery_chance = (10 - self.skill_level) * 0.015
        if random.random() < discovery_chance:
            return "discovered"
        
        return None
    
    def _select_evidence_type(self):
        """Beweistyp basierend auf Skill-Level auswählen."""
        # Bessere Spione finden wertvollere Beweise
        weights = [1, 2, 3, 4, 5]  # bookkeeping, tax_evasion, contract_breach, bribery, forgery
        types = ["bookkeeping", "tax_evasion", "contract_breach", "bribery", "forgery"]
        
        if self.skill_level >= 8:
            weights = [1, 2, 3, 5, 4]  # Mehr Bestechungsnachweise und Fälschungen
        elif self.skill_level >= 5:
            weights = [1, 3, 3, 3, 2]
        
        return random.choices(types, weights=weights)[0]
    
    def _determine_quality(self):
        """Qualität des Beweises bestimmen (1-5)."""
        # Bessere Spione finden qualitativ hochwertigere Beweise
        quality_weights = [1, 2, 3, 4, 5]
        if self.skill_level >= 7:
            quality_weights = [1, 1, 2, 3, 4]
        elif self.skill_level >= 4:
            quality_weights = [1, 2, 3, 3, 2]
        
        return random.choices(range(1, 6), weights=quality_weights)[0]
    
    def get_evidence_value(self):
        """Gesamtwert der gesammelten Beweise."""
        from espionage.evidence import evaluate_evidence
        return evaluate_evidence(self.evidence_collected)
    
    def to_dict(self):
        """Spion serialisieren."""
        return {
            "name": self.name,
            "skill_level": self.skill_level,
            "target": self.target,
            "evidence_collected": self.evidence_collected,
            "mission_rounds": self.mission_rounds
        }


def hire_spy(player, skill_level=None):
    """
    Einen neuen Spion anstellen.
    
    Args:
        player: Spieler-Objekt mit cash und spies Liste
        skill_level: Gewünschtes Skill-Level (1-10), None für zufällig
    
    Returns:
        Tuple von (Spy, Kosten) oder (None, Fehlermeldung)
    """
    if skill_level is None:
        # Zufälliges Skill-Level basierend auf verfügbarem Kapital
        max_affordable = 5
        for level in range(10, 0, -1):
            if SPY_HIRE_COSTS[level] <= player.cash:
                max_affordable = level
                break
        skill_level = random.randint(1, max_affordable)
    
    cost = SPY_HIRE_COSTS[skill_level]
    
    if player.cash < cost:
        return None, f"Nicht genug Geld für Spion mit Skill {skill_level} (benötigt {cost} Gulden)"
    
    # Namen generieren (Schweizer Kontext)
    first_names = ["Hans", "Urs", "Fritz", "Karl", "Peter", "Johann"]
    last_names = ["Müller", "Meier", "Schmid", "Weber", "Huber", "Brunner"]
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    
    player.cash -= cost
    spy = Spy(name, skill_level)
    player.spies.append(spy)
    
    return spy, cost


def pay_spy_maintenance(player):
    """Monatliche Aufrechterhaltungskosten für alle Spione bezahlen."""
    total_cost = 0
    for spy in player.spies:
        total_cost += spy.maintenance_cost
    
    if player.cash < total_cost:
        # Kann nicht zahlen - schlechteste Spione entlassen
        while player.spies and player.cash < total_cost:
            worst_spy = min(player.spies, key=lambda s: s.skill_level)
            player.spies.remove(worst_spy)
            total_cost -= worst_spy.maintenance_cost
    
    player.cash -= total_cost
    return total_cost


def get_available_spies():
    """Liste verfügbarer Spione mit ihren Kosten zurückgeben."""
    available = []
    for level in range(1, 11):
        available.append({
            "skill_level": level,
            "hire_cost": SPY_HIRE_COSTS[level],
            "maintenance_cost": int(SPY_HIRE_COSTS[level] * SPY_MAINTENANCE_FACTOR)
        })
    return available