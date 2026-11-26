# Rechtssystem - Analyse & Spezifikation

## Original-Analyse (Fugger II)

Das Rechtssystem in Fugger II ermöglicht es Spielern, rechtliche Streitigkeiten zu führen und zu lösen. Es ist eng mit dem Spionagesystem verbunden.

### Kernfunktionen
1. **Gerichtsverhandlungen**: Formelle Prozesse vor einem Gericht
2. **Zeugen**: Einberufung von Zeugen zur Aussage
3. **Plädoyers**: Anwälte halten Plädoyers für beide Seiten
4. **Bestechung**: Möglichkeit, das Gericht zu bestechen (optional ein-/ausschaltbar)
5. **Beweisführung**: Vorlage gesammelter Beweise (aus dem Spionagesystem)

### Spielmechanik
- Spieler kann Prozess gegen Rivalen anstrengen (bei ausreichender Beweislage)
- Rival kann auch Prozess gegen Spieler anstrengen
- Gerichtsverfahren dauern mehrere Spielrunden
- Ergebnis hängt von Beweisen, Zeugen und Anwaltsgewandtheit ab
- Bestechung verbessert Chancen auf günstiges Urteil

### Optionen im Spiel
- **"Gericht bestechen"**: Kann im Optionsmenü ein-/ausgeschaltet werden (standardmäßig eingeschaltet)
  - Wenn ausgeschaltet: Schlechtere Ausgangsposition vor Gericht, aber faire Verfahren
- **"Zeugen und Plädoyers überspringen"**: Schnelleres Gerichtsverfahren ohne Details

## Umsetzung in Confoederatio Helvetica

### Schweizer Kontext
Die Schweizer Konföderation hatte ein komplexes Rechtssystem mit:
- Kantonalen Gerichten für lokale Streitigkeiten
- Bundesgerichten für zwischenkantonale Konflikte
- Handelsrecht für wirtschaftliche Streitigkeiten
- Vertragsrecht für Handelsverträge

### Gerichtstypen
1. **Handelsgericht**: Wirtschaftsstreitigkeiten, Vertragsbrüche
2. **Kantonsgericht**: Lokale Rechtsstreitigkeiten
3. **Bundesgericht**: Zwischenkantonale Konflikte, große Fälle

### Prozessablauf (Vorschlag)
```python
class CourtCase:
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
        if side == "plaintiff":
            self.evidence_plaintiff.append(evidence)
        else:
            self.evidence_defendant.append(evidence)
    
    def calculate_verdict(self):
        # Beweise bewerten
        plaintiff_score = sum(e.quality * EVIDENCE_VALUES[e.type] for e in self.evidence_plaintiff)
        defendant_score = sum(e.quality * EVIDENCE_VALUES[e.type] for e in self.evidence_defendant)
        
        # Zeugen hinzufügen
        plaintiff_score += len(self.witnesses_plaintiff) * 10
        defendant_score += len(self.witnesses_defendant) * 10
        
        # Bestechungsfaktor (falls aktiviert)
        if bribery_enabled:
            plaintiff_score += self.plaintiff.bribe_amount * 0.5
            defendant_score += self.defendant.bribe_amount * 0.5
        
        # Zufallsfaktor für Realismus
        random_factor = random.randint(-10, 10)
        
        if plaintiff_score + random_factor > defendant_score:
            return "plaintiff_wins"
        else:
            return "defendant_wins"
```

### Bestechungssystem
- Spieler kann Richter bestechen für günstigeres Urteil
- Bestechungsbetrag beeinflusst Ergebnis proportional
- Risiko: Wenn entdeckt, zusätzliche Strafe und Rufschädigung
- Option im Optionsmenü zum Deaktivieren (faire Verfahren)

### Zeugen & Plädoyers
- **Zeugen**: Können einberufen werden, erhöhen Chancen auf Sieg
  - Kosten pro Zeuge
  - Qualität variiert (einige sind überzeugender als andere)
- **Plädoyers**: Anwälte halten Reden für beide Seiten
  - Kann übersprungen werden (Option im Optionsmenü)
  - Hinzufügt Dramatik und Spannung zum Verfahren

### Konsequenzen von Prozessen
1. **Sieg**: Schadensersatz, Vertragsdurchsetzung, Rufgewinn
2. **Niederlage**: Zahlung an Gegner, Vertragsstrafe, Rufverlust
3. **Unentschieden**: Keine Partei gewinnt, aber Kosten für beide

## Technische Umsetzung

### Dateien
- `court.py`: Gerichtsverfahren, Prozessablauf, Urteilsfindung
- `bribery.py`: Bestechungssystem, Risiko-Berechnung

### Datenstrukturen
```python
class CourtCase:
    id: int
    plaintiff: Player
    defendant: Player
    case_type: str  # "trade_dispute", "contract_breach", etc.
    evidence_plaintiff: list[Evidence]
    evidence_defendant: list[Evidence]
    witnesses_plaintiff: list[Witness]
    witnesses_defendant: list[Witness]
    status: str  # "filed", "hearing", "verdict"
    verdict: str  # "plaintiff_wins", "defendant_wins", "draw"
    
class Witness:
    name: str
    credibility: int  # 1-10
    side: str  # "plaintiff" or "defendant"
```

## Offene Fragen
1. Wie komplex soll das Rechtssystem sein? (Einfache Punktzahl vs. detaillierte Beweisführung)
2. Sollen Spieler eigene Anwälte anstellen können mit unterschiedlichen Fähigkeiten?
3. Wie werden Zeugen gefunden und einberufen?
4. Sollen es verschiedene Rechtsgebiete geben (Handelsrecht, Strafrecht, etc.)?