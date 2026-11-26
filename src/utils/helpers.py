"""
Allgemeine Hilfsfunktionen.
"""

import random


def format_money(amount):
    """Betrag als Geldbetrag formatieren."""
    return f"{amount:,.2f} Gulden"


def chance(percent):
    """Prüfe ob ein Ereignis mit gegebener Wahrscheinlichkeit eintritt."""
    return random.random() * 100 < percent


def weighted_choice(options):
    """Gewichtete Zufallsauswahl."""
    total_weight = sum(option['weight'] for option in options)
    rand = random.uniform(0, total_weight)
    
    cumulative = 0
    for option in options:
        cumulative += option['weight']
        if rand <= cumulative:
            return option
    
    return options[-1]