"""
Gerichtsverfahren - Prozesse und Urteilsfindung.

Formelle Prozesse vor einem Gericht mit Zeugen, Plädoyers und Beweisen.
Basierend auf dem Fugger II System mit Schweizer Rechtskontext.
"""

import random


class Witness:
    """Ein Zeuge im Gerichtsverfahren."""
    
    def __init__(self, name, credibility):
        self.name = name
        self.credibility = credibility  # 1-10
    
    @property
    def impact(self):
        """Auswirkung des Zeugen auf das Urteil (Punkte)."""
        return self.credibility * 2


class CourtCase:
    """Ein Gerichtsverfahren."""
    
    def __init__(self, plaintiff, defendant, case_type="trade_dispute"):
        self.id = random.randint(1000, 9999)
        self.plaintiff = plaintiff
        self.defendant = defendant
        self.case_type = case_type
        self.evidence_plaintiff = []
        self.evidence_defendant = []
        self.witnesses_plaintiff = []
        self.witnesses_defendant = []
        self.status = "filed"  # filed, hearing, verdict
        self.verdict = None
        self.bribe_amount_plaintiff = 0
        self.bribe_amount_defendant = 0
    
    def add_evidence(self, side, evidence):
        """Beweis hinzufügen."""
        if side == "plaintiff":
            self.evidence_plaintiff.append(evidence)
        else:
            self.evidence_defendant.append(evidence)
    
    def add_witness(self, side, witness):
        """Zeuge hinzufügen."""
        if side == "plaintiff":
            self.witnesses_plaintiff.append(witness)
        else:
            self.witnesses_defendant.append(witness)
    
    def set_bribe_amount(self, side, amount):
        """Bestechungsbetrag setzen."""
        if side == "plaintiff":
            self.bribe_amount_plaintiff = amount
        else:
            self.bribe_amount_defendant = amount
    
    def calculate_scores(self, bribery_enabled=True):
        """Punktzahlen für beide Seiten berechnen."""
        from espionage.evidence import evaluate_evidence
        
        # Beweise bewerten
        plaintiff_score = evaluate_evidence(self.evidence_plaintiff)
        defendant_score = evaluate_evidence(self.evidence_defendant)
        
        # Zeugen hinzufügen
        for witness in self.witnesses_plaintiff:
            plaintiff_score += witness.impact
        for witness in self.witnesses_defendant:
            defendant_score += witness.impact
        
        # Bestechungsfaktor (falls aktiviert)
        if bribery_enabled:
            from legal.bribery import calculate_bribe_effectiveness
            difficulty = 5  # Durchschnittliche Schwierigkeit
            
            plaintiff_bribe_bonus = calculate_bribe_effectiveness(
                self.bribe_amount_plaintiff, difficulty
            )
            defendant_bribe_bonus = calculate_bribe_effectiveness(
                self.bribe_amount_defendant, difficulty
            )
            
            plaintiff_score += plaintiff_bribe_bonus
            defendant_score += defendant_bribe_bonus
        
        return plaintiff_score, defendant_score
    
    def calculate_verdict(self, bribery_enabled=True):
        """Urteil berechnen."""
        self.status = "hearing"
        
        plaintiff_score, defendant_score = self.calculate_scores(bribery_enabled)
        
        # Zufallsfaktor für Realismus (±15 Punkte)
        random_factor = random.randint(-15, 15)
        
        final_plaintiff = plaintiff_score + random_factor
        final_defendant = defendant_score
        
        if final_plaintiff > final_defendant:
            self.status = "verdict"
            self.verdict = "plaintiff_wins"
            return "plaintiff_wins", {
                "plaintiff_score": int(plaintiff_score),
                "defendant_score": int(defendant_score),
                "random_factor": random_factor,
                "final_plaintiff": int(final_plaintiff),
                "final_defendant": int(final_defendant)
            }
        elif final_defendant > final_plaintiff:
            self.status = "verdict"
            self.verdict = "defendant_wins"
            return "defendant_wins", {
                "plaintiff_score": int(plaintiff_score),
                "defendant_score": int(defendant_score),
                "random_factor": random_factor,
                "final_plaintiff": int(final_plaintiff),
                "final_defendant": int(final_defendant)
            }
        else:
            self.status = "verdict"
            self.verdict = "draw"
            return "draw", {
                "plaintiff_score": int(plaintiff_score),
                "defendant_score": int(defendant_score),
                "random_factor": random_factor,
                "final_plaintiff": int(final_plaintiff),
                "final_defendant": int(final_defendant)
            }
    
    def get_case_summary(self):
        """Zusammenfassung des Falls zurückgeben."""
        from espionage.evidence import evaluate_evidence
        
        plaintiff_score = evaluate_evidence(self.evidence_plaintiff)
        defendant_score = evaluate_evidence(self.evidence_defendant)
        
        return {
            "case_id": self.id,
            "plaintiff": self.plaintiff.name if hasattr(self.plaintiff, 'name') else str(self.plaintiff),
            "defendant": self.defendant.name if hasattr(self.defendant, 'name') else str(self.defendant),
            "case_type": self.case_type,
            "status": self.status,
            "verdict": self.verdict,
            "plaintiff_evidence_score": plaintiff_score,
            "defendant_evidence_score": defendant_score,
            "witnesses_plaintiff": len(self.witnesses_plaintiff),
            "witnesses_defendant": len(self.witnesses_defendant)
        }


def hire_witness(player, side="plaintiff"):
    """
    Einen Zeugen anstellen.
    
    Args:
        player: Spieler-Objekt mit cash
        side: "plaintiff" oder "defendant"
    
    Returns:
        Tuple von (Witness, Kosten) oder (None, Fehlermeldung)
    """
    # Kosten für Zeuge basierend auf Glaubwürdigkeit
    credibility = random.randint(3, 8)
    cost = credibility * 25
    
    if player.cash < cost:
        return None, f"Nicht genug Geld für Zeuge (benötigt {cost} Gulden)"
    
    # Namen generieren
    first_names = ["Anna", "Maria", "Elisabeth", "Katharina", "Margareta"]
    last_names = ["Bauer", "Fischer", "Wagner", "Schneider", "Keller"]
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    
    player.cash -= cost
    witness = Witness(name, credibility)
    
    return witness, cost


def get_case_type_description(case_type):
    """Beschreibung des Falltyps zurückgeben."""
    descriptions = {
        "trade_dispute": "Handelsstreitigkeit",
        "contract_breach": "Vertragsbruch",
        "tax_evasion": "Steuerhinterziehung",
        "bribery": "Bestechung",
        "forgery": "Fälschung"
    }
    return descriptions.get(case_type, case_type)