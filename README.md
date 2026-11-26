# Confoederatio Helvetica - Wirtschaftssimulation

Eine Schweizer Wirtschaftssimulation im Renaissance-Stil, inspiriert von historischen Handels- und Bankgeschäften der Eidgenossenschaft.

## 🎯 Vision

Der Spieler übernimmt die Rolle eines aufstrebenden Kaufmanns/Bankiers in der Schweizer Konföderation des 15./16. Jahrhunderts. Ziel ist es, durch kluges Handeln, strategische Allianzen und geschickte Manöver ein florierendes Handelsimperium aufzubauen - während historische Ereignisse das Spielgeschehen prägen.

## 📜 Rote Linie - Entwicklungsplan

### Phase 1: Grundgerüst (Aktuell)
- [x] Projektstruktur erstellt
- [x] Dokumentationsdateien angelegt
- [ ] Hauptmenü mit Pygame implementieren
- [ ] Spielzustands-Management aufbauen
- [ ] Speichern/Laden mit SQLite implementieren

### Phase 2: Wirtschaftssystem
- [ ] Handel zwischen Städten implementieren
- [ ] Preisberechnung (Angebot/Nachfrage)
- [ ] Bankwesen & Kreditverwaltung
- [ ] Auktionssystem

### Phase 3: Spionage & Recht
- [ ] Spionagesystem mit Beweissammlung
- [ ] Gerichtsverhandlungen
- [ ] Bestechungssystem
- [ ] Zeugen & Plädoyers

### Phase 4: Militär & Kämpfe
- [ ] Schlachtensystem
- [ ] Belagerungen
- [ ] KI-General-Steuerung (ESC-Taste-Funktion)
- [ ] Eskortierte Transporte

### Phase 5: Ereignisse & Abenteuer
- [ ] Historische Ereignisse pro Jahr
- [ ] Sub-Plots/Abenteuer implementieren
- [ ] Zufallsmeldungen ("Schicksal")
- [ ] Hilfen von erfahrenen Kaufleuten

### Phase 6: Mehrspieler & Polish
- [ ] Rundenbasiertes Mehrspieler-Spiel
- [ ] Spieler-Ankündigungen
- [ ] Sound & Musik integrieren
- [ ] Grafiken optimieren
- [ ] Bugfixing & Testing

## 🏗️ Architektur

### Technologie-Stack
- **GUI**: Pygame (spielähnliche Oberfläche mit Sprites und Animationen)
- **Datenhaltung**: SQLite (Speicherspiele und persistente Daten)
- **Audio**: pygame.mixer (Soundeffekte und Musik)
- **Bildverarbeitung**: Pillow (für Bildmanipulation)

### Projektstruktur
```
confoederatio-helvetica/
├── src/                    # Quellcode
│   ├── economy/            # Wirtschaftssystem (Handel, Bankwesen, Preise)
│   ├── espionage/          # Spionagesystem
│   ├── legal/              # Rechtssystem (Gerichte, Bestechung)
│   ├── military/           # Militärsystem (Schlachten, Belagerungen)
│   ├── events/             # Ereignisse & Abenteuer
│   ├── ui/                 # Benutzeroberfläche
│   └── utils/              # Hilfsfunktionen & Tools
├── assets/                 # Grafiken, Sounds, Musik
├── data/                   # Szenarien & Speicherspiele
├── tests/                  # Unit Tests
└── docs/                   # Dokumentation
```

## 📚 Subsystem-Dokumentation

Jedes Subsystem hat eine eigene README.md mit detaillierter Analyse:

- [Wirtschaftssystem](src/economy/README.md) - Handel, Bankwesen, Preise
- [Spionagesystem](src/espionage/README.md) - Spione & Beweissammlung
- [Rechtssystem](src/legal/README.md) - Gerichte & Bestechung
- [Militärsystem](src/military/README.md) - Schlachten & Belagerungen
- [Ereignisse](src/events/README.md) - Historische Ereignisse & Abenteuer
- [Benutzeroberfläche](src/ui/README.md) - UI-Komponenten
- [Hilfsfunktionen](src/utils/README.md) - Tools & Utilities

## 🎮 Spielmerkmale (basierend auf Original-Analyse)

### Wirtschaft
- Handel zwischen Schweizer Städten und internationalen Handelspartnern
- Dynamische Preisbildung basierend auf Angebot/Nachfrage
- Bankwesen mit Krediten, Zinsen und Wechselgeschäften
- Auktionen für seltene Güter und Kunstwerke

### Spionage & Intrigen
- Anstellung von Spionen zur Überwachung von Rivalen
- Sammlung von Beweisen für Gerichtsverfahren
- Sabotage und Wirtschaftsspionage

### Rechtssystem
- Gerichtsverhandlungen mit Zeugen und Plädoyers
- Bestechungsmöglichkeiten (optional ein-/ausschaltbar)
- Vertragsstreitigkeiten und Eigentumsfragen

### Militär
- Militärische Feldzüge zur Sicherung von Handelsrouten
- Belagerungen von Städten
- Eskortierte Transporte gegen Räuber
- KI-General übernimmt bei Bedarf die Führung (ESC-Taste)

### Historische Ereignisse
- Jahr-für-Jahr historische Narrative der Schweizer Geschichte
- Über 30 Sub-Plots/Abenteuer über mehrere Jahre hinweg
- Zufallsmeldungen ("Schicksal") für zusätzliche Spannung
- Hilfreiche Tipps von erfahrenen Kaufleuten

## ⚙️ Konfiguration & Optionen

Das Spiel bietet folgende Einstellmöglichkeiten:
- Spieldauer bis ins Jahr 1800 erweiterbar
- Gerichtsbestechung ein-/ausschaltbar
- Historische Ereignisse ein-/ausschaltbar
- Abenteuer/Sub-Plots ein-/ausschaltbar
- Zufallsmeldungen ein-/ausschaltbar
- Hilfen ein-/ausschaltbar
- Sound und Grafik-Einstellungen

## 🌍 Schweizer Kontext

Anstatt der deutschen Fugger-Familie spielt das Spiel in der Schweizer Konföderation:
- Historische Städte: Zürich, Basel, Genf, Bern, Luzern
- Schweizer Handelsrouten über die Alpen
- Historische Ereignisse der Schweizer Geschichte
- Schweizer Banktradition und Wirtschaftsgeschichte

## 🚀 Starten des Spiels

```bash
# Abhängigkeiten installieren
pip install -r requirements.txt

# Spiel starten
python src/main.py
```

## 📝 Entwicklungshinweise

- Alle Texte auf Deutsch (Standardsprache)
- Code-Kommentare können auf Englisch sein
- Git Commits auf Englisch mit klaren Beschreibungen
- Tests für alle kritischen Funktionen schreiben