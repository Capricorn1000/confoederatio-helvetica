"""
Beweissammlung und -bewertung.
"""


# Werte für verschiedene Beweistypen
EVIDENCE_VALUES = {
    "bookkeeping": 10,      # Buchhaltungsfehler
    "tax_evasion": 25,      # Steuerhinterziehung
    "contract_breach": 15,  # Vertragsbruch
    "bribery": 30,          # Bestechungsnachweise
    "forgery": 20           # Fälschungen
}


def evaluate_evidence(evidence_list):
    """Gesamtwert einer Beweissammlung bewerten."""
    total = 0
    for evidence in evidence_list:
        value = EVIDENCE_VALUES.get(evidence["type"], 5) * evidence["quality"]
        total += value
    return total


def can_file_lawsuit(evidence_value):
    """Prüfen ob genug Beweise für einen Prozess vorhanden sind."""
    return evidence_value >= 50