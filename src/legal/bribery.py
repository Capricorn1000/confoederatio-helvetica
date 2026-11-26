"""
Bestechungssystem - Richter bestechen für günstigeres Urteil.

Spieler können Richter bestechen, um das Ergebnis eines Gerichtsverfahrens
zu beeinflussen. Das Risiko der Entdeckung steigt mit dem Betrag.
Basierend auf dem Fugger II System (optional ein-/ausschaltbar).
"""

import random


def calculate_bribe_effectiveness(amount, difficulty=5):
    """
    Wirksamkeit einer Bestechung berechnen.
    
    Args:
        amount: Bestechungsbetrag in Gulden
        difficulty: Schwierigkeit des Falls (1-10), höher = schwerer zu bestechen
    
    Returns:
        Bonus-Punkte für das Urteil
    """
    if amount <= 0:
        return 0
    
    base_effectiveness = amount * 0.5
    
    # Höhere Schwierigkeit reduziert Wirksamkeit
    difficulty_factor = max(1.0 - (difficulty * 0.08), 0.2)
    
    return base_effectiveness * difficulty_factor


def risk_of_discovery(amount, skill_level=5):
    """
    Risiko der Entdeckung berechnen.
    
    Args:
        amount: Bestechungsbetrag (höheres Risiko bei größeren Beträgen)
        skill_level: Geschicklichkeit des Bestechers (1-10), höher = weniger Risiko
    
    Returns:
        Wahrscheinlichkeit der Entdeckung (0.0 - 1.0)
    """
    if amount <= 0:
        return 0.0
    
    base_risk = min(amount * 0.002, 0.7)
    
    # Bessere Geschicklichkeit reduziert Risiko
    skill_factor = max(1.0 - (skill_level * 0.06), 0.3)
    
    return min(base_risk * skill_factor, 0.9)


def check_bribe_discovery(amount, skill_level=5):
    """
    Prüfen ob eine Bestechung entdeckt wurde.
    
    Args:
        amount: Bestechungsbetrag
        skill_level: Geschicklichkeit des Bestechers
    
    Returns:
        True wenn entdeckt, False sonst
    """
    risk = risk_of_discovery(amount, skill_level)
    return random.random() < risk


def get_bribe_suggestions():
    """Vorschläge für Bestechungsbeträge zurückgeben."""
    return [
        {"amount": 50, "description": "Kleine Geste"},
        {"amount": 150, "description": "Mäßige Bestechung"},
        {"amount": 300, "description": "Erhebliche Summe"},
        {"amount": 500, "description": "Großzügiges Angebot"}
    ]


def get_discovery_consequences():
    """Konsequenzen bei Entdeckung einer Bestechung."""
    return {
        "fine": "Geldstrafe (doppelter Bestechungsbetrag)",
        "reputation": "Rufschädigung (-10 Rufpunkte)",
        "case_dismissed": "Fall wird abgewiesen"
    }