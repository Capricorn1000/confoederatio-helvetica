# Confoederatio Helvetica

Eine Schweizer Wirtschaftssimulation im Renaissance-Stil (1500-1600).
Basierend auf dem Spielkonzept von Fugger II.

## Kapitel-Fortschritt

### ✅ Kapitel 1: Kern-Spiel-Loop & Wirtschaftssystem
- Handel zwischen Zürich, Basel, Genf, Bern, Luzern
- Preisschwankungen und Angebot/Nachfrage
- Warentransport und Gewinne

### ✅ Kapitel 2: Spionage & Rechtssystem
- Spione anstellen und verwalten
- Beweise sammeln
- Gerichtsverfahren und Bestechung

### ✅ Kapitel 3: Militärsystem & Truppenverwaltung
- Truppentypen: Hellebardiere, Armbrustschützen, Reiter
- Schlachten und Belagerungen
- Kantonale Konflikte

### ✅ Kapitel 4: Ereignisse & Abenteuer
- 28 historische Narrative
- 30 mehrjährige Sub-Plots
- Zufallsmeldungen "Schicksal"
- Hilfetipps von erfahrenen Kaufleuten

### ✅ Kapitel 5: Benutzeroberfläche & Spielsteuerung
- Hauptmenü mit Speichern/Laden
- Optionen-Menü
- Ereignis-Anzeigefenster
- Abenteuer-Auswahlmenü
- Kartenansicht mit Routen
- Truppenverwaltung, Spionage-Dashboard, Gerichtsverfahrens-Schnittstelle

### ✅ Kapitel 6: Sound, Musik & Grafiken
- SoundManager mit Pygame.mixer
- GraphicsManager mit Renaissance-Farbschema
- Stadt-/Güter-/Truppen-Icons
- Hintergrundmusik und Soundeffekte

### ✅ Kapitel 7: Mehrspieler & Polish
- Hotseat-Mehrspieler (2-4 Spieler)
- Spieler-Einrichtung mit Namen/Farben
- Sichtbarkeitsregeln
- Siegbedingungen (Vermögen oder Jahre)
- Rundenverwaltung

### ✅ Kapitel 8: Grafiken, Assets & Finaler Polish
- **Echte Renaissance-Grafiken**: Programmatisch generierte Assets mit Pillow
  - Detaillierte Stadt-Icons für alle 5 Kantone (gotische Architektur)
  - Historische Güter-Icons (Getreide-Säcke, Wein-Fässer, Käse-Räder, etc.)
  - Truppen-Icons in Schweizer Tracht
  - Titelbildschirm mit dekorativem Renaissance-Rahmen
  - Pergament-texturierte Kartenhintergründe
- **Performance-Optimierung**:
  - LRU-Cache für häufige Berechnungen (Preise, Truppenstärken)
  - Memoization-Decorator für teure Funktionen
  - Objekt-Pooling für Ressourcenverwaltung
  - Optimiert für 50+ Jahre Spielzeit ohne Speicherlecks
- **Effiziente Serialisierung**:
  - Gzip-Kompression für große Spielstände
  - Kompakte JSON-Formatierung
  - Inkrementelle Speichermöglichkeiten
- **Umfassende Tests**:
  - Performance-Tests (Cache, Memoization, Pooling)
  - Save/Load-Tests mit großen Spielständen
  - Mehrspieler-Szenario-Tests
  - Spielbalance-Validierung
- **Spielbalance-Anpassungen**:
  - Zentrale Balance-Konfiguration (`src/config/balance.py`)
  - Kalibrierte Wirtschaftswerte für fairen Mehrspieler-Wettbewerb
  - Ausgewogene Truppenkosten und -stärken
  - Optimierte Ereignis-Frequenz

## Installation

```bash
pip install -r requirements.txt
```

## Asset-Generierung

Alle Grafiken werden programmatisch mit Pillow generiert:

```bash
python src/assets/generate_assets.py
```

Dies erstellt:
- `assets/cities/` - Stadt-Icons für alle 5 Kantone
- `assets/goods/` - Güter-Icons (6 Typen)
- `assets/troops/` - Truppen-Icons (3 Typen)
- `assets/title_screen.png` - Titelbildschirm
- `assets/map_background.png` - Kartenhintergrund

## Spiel starten

```bash
python src/main.py
```

## Tests ausführen

```bash
python -m pytest tests/
# oder einzelne Testdateien:
python -m unittest tests.test_performance
python -m unittest tests.test_save_load
python -m unittest tests.test_multiplayer
```

## Projektstruktur

```
confoederatio-helvetica/
├── src/
│   ├── main.py              # Einstiegspunkt
│   ├── game.py              # Haupt-Spiel-Loop (optimiert)
│   ├── game_state.py        # Spielzustand
│   ├── config/              # Konfiguration & Balance-Werte
│   │   └── balance.py       # Zentrale Spielbalance
│   ├── economy/             # Wirtschaftssystem
│   ├── espionage/           # Spionagesystem
│   ├── events/              # Ereignisse & Abenteuer
│   ├── legal/               # Rechtssystem
│   ├── military/            # Militärsystem
│   ├── ui/                  # Benutzeroberfläche
│   ├── utils/               # Hilfsprogramme
│   │   ├── performance.py   # Performance-Optimierung & Caching
│   │   ├── graphics_manager.py  # Grafikverwaltung
│   │   └── save_load.py     # Optimiertes Speichern/Laden
│   └── assets/              # Generierte Grafiken
│       └── generate_assets.py
├── tests/                   # Test-Suite
│   ├── test_performance.py
│   ├── test_save_load.py
│   └── test_multiplayer.py
├── docs/                    # Dokumentation
├── assets/                  # Generierte Assets (Output)
└── requirements.txt
```

## Lizenz

MIT License
