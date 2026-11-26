# Militärsystem - Analyse & Spezifikation

## Original-Analyse (Fugger II)

Das Militärsystem in Fugger II ermöglicht es Spielern, militärische Aktionen durchzuführen und ihre Handelsrouten zu schützen.

### Kernfunktionen
1. **Schlachten**: Gefechte zwischen Truppen
2. **Belagerungen**: Belagerung von Städten (gekennzeichnet durch gekreuzte goldene Schwerter auf der Karte)
3. ** Eskortierte Transporte**: Schutz von Handelsgütern vor Räubern
4. **KI-General-Steuerung**: Bei Drücken der ESC-Taste übernimmt ein Computer-gesteuerter General die Führung der Truppen

### Spielmechanik
- Spieler kann eigene Truppen rekrutieren und ausrüsten
- Militärische Aktionen sind riskant und teuer
- Eskortierte Transporte schützen vor Räubereien auf Handelsrouten
- Belagerungen dauern mehrere Spielrunden
- KI-General kann Schlachten führen, wenn Spieler nicht eingreifen möchte

### Optionen im Spiel
- **Kampfgeschehen verkürzen**: ESC-Taste während Gefecht übernimmt KI-General die Führung
  - Spieler kann jederzeit wieder eingreifen durch Drücken des Hotkeys (festgelegt zu Spielbeginn)

## Umsetzung in Confoederatio Helvetica

### Schweizer Kontext
Die Schweizer Konföderation war im 15./16. Jahrhundert für ihre militärische Stärke bekannt:
- Schweizer Söldner waren die besten Kämpfer Europas
- Die Eidgenossen verteidigten ihre Unabhängigkeit gegen Habsburger und andere Mächte
- Militärische Konflikte um Handelsrouten über die Alpen

### Truppentypen (historisch inspiriert)
1. **Schildknappen**: Leicht gepanzerte Infanterie mit Lanzen
2. **Hellebardiere**: Schwerinfanterie mit Hellebarden (schweizer Spezialität)
3. **Armbrustschützen**: Fernkämpfer mit Armbrüsten
4. **Reiter**: Kavallerie für schnelle Angriffe und Verfolgung
5. **Söldner**: Professionelle Kämpfer aus verschiedenen Regionen

### Schlachtensystem (Vorschlag)
```python
class Battle:
    def __init__(self, attacker, defender, location):
        self.attacker = attacker
        self.defender = defender
        self.location = location
        self.turns = 0
    
    def resolve_turn(self):
        self.turns += 1
        
        # Angreifer attackiert
        attacker_damage = self.calculate_damage(self.attacker)
        self.defender.health -= attacker_damage
        
        if self.defender.health <= 0:
            return "attacker_wins"
        
        # Verteidiger kontert
        defender_damage = self.calculate_damage(self.defender)
        self.attacker.health -= defender_damage
        
        if self.attacker.health <= 0:
            return "defender_wins"
        
        return "ongoing"
    
    def calculate_damage(self, side):
        base_damage = side.troops * side.weapon_factor
        terrain_bonus = self.get_terrain_modifier(side)
        morale_factor = side.morale / 100.0
        
        return int(base_damage * terrain_bonus * morale_factor)
```

### Belagerungssystem
- Belagerungen dauern mehrere Spielrunden (Wochen/Monate im Spiel)
- Verteidiger hat Vorteil durch Mauern und Festungsanlagen
- Angreifer muss Versorgungslinien aufrechterhalten
- Möglichkeit zur Kapitulation oder Aushungerung

### Eskortierte Transporte
- Spieler kann Truppen zum Schutz von Handelsgütern einsetzen
- Gekennzeichnet durch gekreuzte Schwerter (X) im Spiel
- Reduziert Risiko von Räubereien erheblich
- Kosten für Truppen und Verpflegung während des Transports

### KI-General-Steuerung
```python
class AI_General:
    def __init__(self, difficulty):
        self.difficulty = difficulty  # easy, medium, hard
    
    def make_decision(self, battle_state):
        if battle_state.attacker.health < battle_state.defender.health * 0.5:
            return "retreat"
        
        if battle_state.turns > 10 and self.difficulty == "easy":
            return "negotiate"
        
        # Standard: Weiterkämpfen
        return "fight"
```

### Truppenverwaltung
- Rekrutierung in verschiedenen Städten
- Ausrüstung und Training verbessern Kampfkraft
- Moral beeinflusst Kampfleistung
- Verpflegung und Unterhalt kosten Geld pro Runde

## Technische Umsetzung

### Dateien
- `battles.py`: Schlachtensystem, Kampfauflösung
- `sieges.py`: Belagerungssystem, Festungsbelagerungen
- `ai_general.py`: KI-General-Steuerung, Entscheidungslogik

### Datenstrukturen
```python
class Troop:
    type: str  # "halberdier", "crossbowman", "knight", etc.
    count: int
    health: int
    morale: int
    weapon_factor: float
    
class Battle:
    attacker: Troop
    defender: Troop
    location: City
    turns: int
    status: str  # "ongoing", "attacker_wins", "defender_wins"
```

## Offene Fragen
1. Wie komplex soll das Schlachtensystem sein? (Einfach vs. taktisch)
2. Sollen Spieler eigene Festungen bauen und verteidigen können?
3. Wie werden Truppenbewegungen auf der Karte dargestellt?
4. Soll es verschiedene Waffentypen mit Vor- und Nachteilen geben?