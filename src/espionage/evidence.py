"""
Beweissammlung und -bewertung.

Verschiedene Beweistypen mit unterschiedlichem Wert für Gerichtsverfahren.
Basierend auf dem Fugger II System mit Schweizer Handelskontext.
"""


# Werte für verschiedene Beweistypen (basierend auf Schwere des Vergehens)
EVIDENCE_VALUES = {
    "bookkeeping": 10,      # Buchhaltungsfehler - geringfügig
    "tax_evasion": 25,      # Steuerhinterziehung - schwerwiegend
    "contract_breach": 15,  # Vertragsbruch - mittel
    "bribery": 30,          # Bestechungsnachweise - sehr schwerwiegend
    "forgery": 20           # Fälschungen - schwerwiegend
}

# Mindestwert für einen Prozess
LAWSUIT_THRESHOLD = 50


def evaluate_evidence(evidence_list):
    """
    Gesamtwert einer Beweissammlung bewerten.
    
    Args:
        evidence_list: Liste von Beweis-Dictionaries mit "type" und "quality"
    
    Returns:
        Gesamtpunktzahl der Beweise
    """
    total = 0
    for evidence in evidence_list:
        value = EVIDENCE_VALUES.get(evidence["type"], 5) * evidence["quality"]
        total += value
    return total


def can_file_lawsuit(evidence_value):
    """Prüfen ob genug Beweise für einen Prozess vorhanden sind."""
    return evidence_value >= LAWSUIT_THRESHOLD


def get_evidence_description(evidence_type, quality):
    """Beschreibung eines Beweises zurückgeben."""
    descriptions = {
        "bookkeeping": f"Buchhaltungsfehler (Qualität {quality}/5)",
        "tax_evasion": f"Steuerhinterziehungsnachweis (Qualität {quality}/5)",
        "contract_breach": f"Vertragsbruchdokumentation (Qualität {quality}/5)",
        "bribery": f"Bestechungsnachweise (Qualität {quality}/5)",
        "forgery": f"Fälschungsnachweis (Qualität {quality}/5)"
    }
    return descriptions.get(evidence_type, f"Beweis (Qualität {quality}/5)")


def get_evidence_value_range():
    """Wertebereich für Beweise zurückgeben."""
    min_val = min(EVIDENCE_VALUES.values())
    max_val = max(EVIDENCE_VALUES.values()) * 5  # Max Qualität ist 5
    return (min_val, max_val)


def get_lawsuit_threshold():
    """Mindestwert für einen Prozess zurückgeben."""
    return LAWSUIT_THRESHOLD