# Ereignissystem - Analyse & Spezifikation

## Original-Analyse (Fugger II)

Das Ereignissystem in Fugger II fügt dem Spiel historische Tiefe und zusätzliche Herausforderungen hinzu.

### Kernfunktionen
1. **Historische Ereignisse**: Jahr-für-Jahr Schilderung historischer Ereignisse zum jeweiligen Spieljahr
2. **Abenteuer/Sub-Plots**: Über 30 \"Spiele im Spiel\", die über mehrere Jahre hinweg gemeistert werden müssen
3. **Schicksal/Zufallsmeldungen**: Zufällige Ereignisse, die das Spielgeschehen beeinflussen
4. **Hilfen von Jakob Fugger**: Optionale hilfreiche Tipps zur Vorgehensweise während des Spiels

### Optionen im Spiel
- **\"Geschichtsschreibung\"**: Historische Ereignisse ein-/ausschalten
  - Wenn aktiviert: In jeder Spielrunde werden historische Ereignisse zum jeweiligen Jahr angezeigt
- **\"Abenteuer\"**: Sub-Plots ein-/ausschalten
  - Wenn eingeschaltet: Treten über 30 \"Spiele im Spiel\" auf, die über mehrere Jahre gemeistert werden müssen
- **\"Schicksal\"**: Zufallsmeldungen aktivieren/deaktivieren
- **\"Hilfen von Jakob Fugger\"**: Hilfreiche Tipps ein-/ausschalten

## Umsetzung in Confoederatio Helvetica

### Schweizer Kontext
Anstatt deutscher Geschichte wird die Schweizer Geschichte verwendet:

#### Historische Ereignisse (Beispiele)
- **1499**: Schwabenkrieg - Eidgenossen besiegen Habsburger, gewinnen Unabhängigkeit
- **1513**: Italienfeldzüge - Schweizer Söldner erobern Mailand
- **1520er**: Reformation in Zürich unter Ulrich Zwingli
- **1531**: Zweiter Kappelkrieg - Konflikt zwischen reformierten und katholischen Kantonen
- **1567**: Schlacht bei Jora - Letzter großer innerkonföderativer Krieg

#### Abenteuer/Sub-Plots (Schweizer Themen)
1. **Alpenhandel sichern**: Handelsrouten über den Gotthardpass gegen Räuber verteidigen
2. **Bankgeheimnis etablieren**: Schweizer Banktradition aufbauen
3. **Söldnerkapitäne rekrutieren**: Beste Schweizer Söldner für eigene Zwecke gewinnen
4. **Kantonale Konflikte lösen**: Vermittlung zwischen streitenden Kantonen
5. **Reformationskonflikte navigieren**: Wirtschaftliche Chancen in religiösen Spannungen nutzen

### Ereignissystem-Architektur (Vorschlag)
```python
class EventSystem:
    def __init__(self):
        self.historical_events = load_historical_events()
        self.active_adventures = []
        self.random_event_chance = 0.15
    
    def process_year(self, year, game_state):
        # Historisches Ereignis für dieses Jahr
        if year in self.historical_events:
            event = self.historical_events[year]
            self.trigger_historical_event(event, game_state)
        
        # Zufallsereignis prüfen
        if random.random() < self.random_event_chance:
            random_event = self.generate_random_event(game_state)
            self.trigger_random_event(random_event, game_state)
        
        # Aktive Abenteuer fortschreiten lassen
        for adventure in self.active_adventures:
            adventure.advance(game_state)
    
    def trigger_historical_event(self, event, game_state):
        # Ereignis auslösen und Auswirkungen auf Spiel anwenden
        print(f\"Historisches Ereignis: {event.title}\")
        event.apply_effects(game_state)
```

### Abenteuer-System (Sub-Plots)
```python
class Adventure:
    def __init__(self, id, title, description, duration_years):
        self.id = id
        self.title = title
        self.description = description
        self.duration_years = duration_years
        self.current_year = 0
        self.completed = False
    
    def advance(self, game_state):
        self.current_year += 1
        
        if self.current_year >= self.duration_years:
            self.complete(game_state)
    
    def complete(self, game_state):
        self.completed = True
        # Belohnung oder Konsequenz anwenden
        pass

# Beispiel-Abenteuer
adventures = [
    Adventure(1, \"Alpenhandel sichern\", \"Verteidige die Handelsrouten über den Gotthardpass gegen Räuber.\", 3),
    Adventure(2, \"Bankgeheimnis etablieren\", \"Baue das Schweizer Bankgeheimnis auf und ziehe internationale Kunden an.\", 5),
    Adventure(3, \"Söldnerkapitäne rekrutieren\", \"Gewinne die besten Schweizer Söldner für deine eigenen Zwecke.\", 2),
]
```

### Zufallsereignisse (\"Schicksal\")
- Naturkatastrophen (Überschwemmungen, Ernteausfälle)
- Plötzliche Preisänderungen
- Tod wichtiger Persönlichkeiten
- Entdeckung neuer Handelsrouten
- Politische Umwälzungen

### Hilfesystem
```python
class HelpSystem:
    def get_tip(self, game_state):
        # Basierend auf Spielzustand hilfreichen Tipp geben
        if game_state.player.cash < 1000:
            return \"Dein Kapital ist niedrig. Überlege dir einen Kredit bei der Bank.\"
        
        if not game_state.player.active_trades:
            return \"Du hast keine aktiven Handelsgeschäfte. Kaufe Güter in einer Stadt und verkaufe sie in einer anderen.\"
        
        # ... weitere Tipps basierend auf Spielzustand
```

## Technische Umsetzung

### Dateien
- `historical.py`: Historische Ereignisse, Jahr-für-Jahr-Narrative
- `adventures.py`: Sub-Plots/Abenteuer, Fortschrittsverfolgung

### Datenstrukturen
```python
class HistoricalEvent:
    year: int
    title: str
    description: str
    effects: list[Effect]  # Auswirkungen auf das Spiel
    
class Adventure:
    id: int
    title: str
    description: str
    duration_years: int
    current_year: int
    completed: bool
```

## Offene Fragen
1. Wie viele historische Ereignisse sollen implementiert werden? (Alle Jahre vs. ausgewählte)
2. Sollen Abenteuer optional sein oder müssen sie gemeistert werden?
3. Wie komplex sollen die Auswirkungen von Ereignissen auf das Spiel sein?
4. Sollen Spieler Entscheidungen bei Ereignissen treffen können?