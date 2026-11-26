# Hilfsfunktionen & Tools - Analyse & Spezifikation

## Original-Analyse (Fugger II)

Das Originalspiel verwendet verschiedene Hilfsfunktionen und Tools:
- Speichern/Laden von Spielen
- Konfigurationsverwaltung
- Zufallszahlengenerierung für Ereignisse
- Datums- und Zeitberechnungen
- Textausgabe und Formatierung

## Umsetzung in Confoederatio Helvetica

### 1. Speichern & Laden (`save_load.py`)

Das Spiel muss den aktuellen Zustand speichern und wiederherstellen können.

```python
import sqlite3
import json

class SaveSystem:
    def __init__(self, save_directory="data/saves"):
        self.save_directory = save_directory
    
    def save_game(self, game_state, filename=None):
        if not filename:
            filename = f"save_{game_state.current_year}.json"
        
        filepath = f"{self.save_directory}/{filename}"
        
        # Spielzustand serialisieren und speichern
        state_dict = game_state.to_dict()
        with open(filepath, 'w') as f:
            json.dump(state_dict, f)
        
        return filepath
    
    def load_game(self, filename):
        filepath = f"{self.save_directory}/{filename}"
        
        with open(filepath, 'r') as f:
            state_dict = json.load(f)
        
        # Spielzustand deserialisieren und zurückgeben
        return GameState.from_dict(state_dict)
    
    def list_saves(self):
        # Liste aller Speicherspiele zurückgeben
        pass
```

### 2. Konfigurationsverwaltung (`config.py`)

Verwaltung der Spieleinstellungen und Optionen.

```python
import configparser

class Config:
    def __init__(self, config_file="data/config.ini"):
        self.config = configparser.ConfigParser()
        self.config_file = config_file
        self.load()
    
    def load(self):
        if os.path.exists(self.config_file):
            self.config.read(self.config_file)
    
    def save(self):
        with open(self.config_file, 'w') as f:
            self.config.write(f)
    
    def get_setting(self, section, key, default=None):
        return self.config.get(section, key, fallback=default)
    
    def set_setting(self, section, key, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))
```

### 3. Zufallszahlengenerierung & Wahrscheinlichkeiten

Für zufällige Ereignisse und Wahrscheinlichkeitsberechnungen.

```python
import random

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

def chance(percent):
    """Prüfe ob ein Ereignis mit gegebener Wahrscheinlichkeit eintritt."""
    return random.random() * 100 < percent
```

### 4. Datums- & Zeitberechnungen

Für die Simulation von Zeiträumen im Spiel.

```python
class GameTime:
    def __init__(self, start_year=1500):
        self.current_year = start_year
        self.current_month = 1
    
    def advance_month(self):
        self.current_month += 1
        if self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
    
    def advance_years(self, years):
        self.current_year += years
    
    def get_season(self):
        if self.current_month in [3, 4, 5]:
            return "Frühling"
        elif self.current_month in [6, 7, 8]:
            return "Sommer"
        elif self.current_month in [9, 10, 11]:
            return "Herbst"
        else:
            return "Winter"
```

### 5. Textausgabe & Formatierung

Für konsistente Textdarstellung im Spiel.

```python
def format_money(amount):
    """Betrag als Geldbetrag formatieren."""
    return f"{amount:,.2f} Gulden"

def format_date(year, month):
    """Datum formatieren."""
    months = ["Januar", "Februar", "März", "April", "Mai", "Juni",
              "Juli", "August", "September", "Oktober", "November", "Dezember"]
    return f"{months[month-1]} {year}"

def truncate_text(text, max_length):
    """Text auf maximale Länge kürzen."""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."
```

### 6. Logging & Debugging

Für die Fehlersuche und Spielanalyse.

```python
import logging

def setup_logging(log_file="data/game.log"):
    logger = logging.getLogger("ConfoederatioHelvetica")
    logger.setLevel(logging.DEBUG)
    
    # Datei-Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    
    # Konsolen-Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
```

## Technische Umsetzung

### Dateien
- `save_load.py`: Speichern/Laden von Spielen (JSON/SQLite)
- `helpers.py`: Allgemeine Hilfsfunktionen (Formatierung, Zufall, etc.)

### Datenstrukturen
```python
# Spielzustand für Serialisierung
class GameState:
    def to_dict(self):
        return {
            "current_year": self.current_year,
            "player_cash": self.player.cash,
            "cities": [city.to_dict() for city in self.cities],
            # ... weitere Zustandsdaten
        }
    
    @classmethod
    def from_dict(cls, state_dict):
        game = cls()
        game.current_year = state_dict["current_year"]
        game.player.cash = state_dict["player_cash"]
        # ... weitere Daten wiederherstellen
        return game
```

## Offene Fragen
1. Soll das Spiel automatisch speichern oder nur manuell?
2. Wie viele Speicherslots sollen verfügbar sein?
3. Sollen Cloud-Saves unterstützt werden?
4. Wie detailliert soll das Logging sein?