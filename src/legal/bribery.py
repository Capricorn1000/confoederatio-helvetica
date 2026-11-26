"""
Bestechungssystem - Richter bestechen für günstigeres Urteil.
"""

import random


def calculate_bribe_effectiveness(amount, difficulty):
    """
    Wirksamkeit einer Bestechung berechnen.
    
    Args:
        amount: Bestechungsbetrag
        difficulty: Schwierigkeit des Falls (1-10)
    
    Returns:
        Bonus-Punkte für das Urteil
    """
    base_effectiveness = amount * 0.5
    
    # Höhere Schwierigkeit reduziert Wirksamkeit
    difficulty_factor = 1.0 - (difficulty * 0.05)
    
    return base_effectiveness * difficulty_factor


def risk_of_discovery(amount, skill_level):
    """
    Risiko der Entdeckung berechnen.
    
    Args:
        amount: Bestechungsbetrag (höheres Risiko bei größeren Beträgen)
        skill_level: Geschicklichkeit des Bestechers (1-10)
    
    Returns:
        Wahrscheinlichkeit der Entdeckung (0.0 - 1.0)
    """
    base_risk = amount * 0.001
    skill_factor = 1.0 - (skill_level * 0.05)
    
    return min(base_risk * skill_factor, 0.9)