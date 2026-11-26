# Spionagesystem - Analyse & Spezifikation

## Original-Analyse (Fugger II)

Das Spionagesystem in Fugger II ermöglicht es Spielern, Informationen über Rivalen zu sammeln und strategische Vorteile zu erlangen.

### Kernfunktionen
1. **Spione anstellen**: Spieler können Spione auf Rivalen ansetzen
2. **Beweissammlung**: Spione sammeln Beweise gegen den Zielrivalen
3. **Bewertung der Beweise**: Im Spionagemenü wird die Anzahl gesammelter Beweise angezeigt
4. **Nutzung der Beweise**: Bei ausreichender Beweislage können verschiedene Aktionen unternommen werden:
   - Prozess gegen den Rivalen anstrengen
   - Erpressung
   - Sabotage vorbereiten

### Spielmechanik
- Spione benötigen Zeit, um Beweise zu sammeln (mehrere Spielrunden)
- Risiko entdeckt zu werden
- Kosten für die Anstellung und Aufrechterhaltung von Spionen
- Qualität der Beweise variiert (einige sind wertvoller als andere)

## Umsetzung in Confoederatio Helvetica

### Schweizer Kontext
In der Schweizer Konföderation des 15./16. Jahrhunderts war Wirtschaftsspionage ein wichtiges Instrument:
- Überwachung von Handelsrouten und -partnern
- Spionagetätigkeit zwischen den Kantonen
- Geheimhaltung von Bankgeschäften und Kundeninformationen

### Spionagetypen
1. **Handelsspionage**: Überwachung von Kauf-/Verkaufstransaktionen eines Rivalen
2. **Bankspionage**: Einblick in Kreditvergaben und Wechselgeschäfte
3. **Politische Spionage**: Informationen über bevorstehende politische Entscheidungen
4. **Militärische Spionage**: Informationen über Truppenbewegungen und Verteidigungsanlagen

### Beweiskategorien
1. **Buchhaltungsfehler**: Unregelmäßigkeiten in den Finanzbüchern
2. **Steuerhinterziehung**: Nicht gemeldete Einnahmen oder Vermögen
3. **Vertragsbrüche**: Nicht eingehaltene Handelsverträge
4. **Bestechungsnachweise**: Beweise für Bestechung von Beamten
5. **Fälschungen**: Gefälschte Dokumente oder Münzen

### Spielmechanik (Vorschlag)
```python
class Spy:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level  # 1-10
        self.target = None
        self.evidence_collected = []
    
    def assign_target(self, rival):
        self.target = rival
    
    def collect_evidence(self, game_round):
        if not self.target:
            return
        
        # Chance auf Beweissammlung basierend auf Skill-Level
        chance = self.skill_level * 0.1
        if random.random() < chance:
            evidence_type = random.choice(EVIDENCE_TYPES)
            evidence = Evidence(evidence_type, quality=random.randint(1, 5))
            self.evidence_collected.append(evidence)
        
        # Risiko entdeckt zu werden
        discovery_chance = (10 - self.skill_level) * 0.02
        if random.random() < discovery_chance:
            return "discovered"
    
    def get_evidence_value(self):
        total = 0
        for evidence in self.evidence_collected:
            total += evidence.quality * EVIDENCE_VALUES[evidence.type]
        return total
```

### Nutzung gesammelter Beweise
1. **Gerichtsverfahren**: Bei ausreichender Beweislage Prozess anstrengen (siehe Rechtssystem)
2. **Erpressung**: Rivalen zu Zahlung oder Zugeständnissen zwingen
3. **Öffentliche Bloßstellung**: Ruf des Rivalen schädigen
4. **Sabotage vorbereiten**: Informationen für gezielte Sabotage nutzen

### Kosten & Risiken
- **Anstellungskosten**: Abhängig vom Skill-Level des Spions
- **Aufrechterhaltungskosten**: Monatliche Bezahlung während der Mission
- **Entdeckungsrisiko**: Höheres Risiko bei weniger fähigen Spionen
- **Racheaktionen**: Entdeckter Rival kann Gegenmaßnahmen ergreifen

## Technische Umsetzung

### Dateien
- `spies.py`: Spion-Klasse, Missionsverwaltung, Beweissammlung
- `evidence.py`: Beweis-Klassen, Bewertungssystem, Nutzungsoptionen

### Datenstrukturen
```python
class Evidence:
    type: str  # "bookkeeping", "tax_evasion", "contract_breach", etc.
    quality: int  # 1-5
    collected_at: int  # Game round when collected
    
EVIDENCE_VALUES = {
    "bookkeeping": 10,
    "tax_evasion": 25,
    "contract_breach": 15,
    "bribery": 30,
    "forgery": 20
}
```

## Offene Fragen
1. Wie viele Spione kann ein Spieler gleichzeitig beschäftigen?
2. Sollen Spione auch für eigene Zwecke eingesetzt werden können (z.B. Marktforschung)?
3. Wie komplex soll das Beweissystem sein? (Einfache Punktzahl vs. detaillierte Beweiskette)
4. Sollen Rivalen auch Spione gegen den Spieler einsetzen?