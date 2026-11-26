"""
Gerichtsverfahren - Prozesse und Urteilsfindung.
"""

import random


class CourtCase:
    """Ein Gerichtsverfahren."""
    
    def __init__(self, plaintiff, defendant, case_type):
        self.plaintiff = plaintiff
        self.defendant = defendant
        self.case_type = case_type
        self.evidence_plaintiff = []
        self.evidence_defendant = []
        self.witnesses_plaintiff = []
        self.witnesses_defendant = []
        self.status = "filed"  # filed, hearing, verdict
    
    def add_evidence(self, side, evidence):
        """Beweis hinzufügen."""
        if side == "plaintiff":
            self.evidence_plaintiff.append(evidence)
        else:
            self.evidence_defendant.append(evidence)
    
    def calculate_verdict(self, bribery_enabled=True):
        """Urteil berechnen."""
        # Beweise bewerten
        plaintiff_score = sum(e["quality"] * 10 for e in self.evidence_plaintiff)
        defendant_score = sum(e["quality"] * 10 for e in self.evidence_defendant)
        
        # Zeugen hinzufügen
        plaintiff_score += len(self.witnesses_plaintiff) * 10
        defendant_score += len(self.witnesses_defendant) * 10
        
        # Bestechungsfaktor (falls aktiviert)
        if bribery_enabled:
            plaintiff_bribe = getattr(self.plaintiff, "bribe_amount", 0)
            defendant_bribe = getattr(self.defendant, "bribe_amount", 0)
            plaintiff_score += plaintiff_bribe * 0.5
            defendant_score += defendant_bribe * 0.5
        
        # Zufallsfaktor für Realismus
        random_factor = random.randint(-10, 10)
        
        if plaintiff_score + random_factor > defendant_score:
            self.status = "verdict"
            return "plaintiff_wins"
        else:
            self.status = "verdict"
            return "defendant_wins"