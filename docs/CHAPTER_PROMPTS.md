# Confoederatio Helvetica - Kapitel Start-Prompts

Diese Datei enthält die Start-Prompts für jedes Kapitel der Implementierung. Kopiere den Prompt für das gewünschte Kapitel und starte eine neue Session damit.

---

## Kapitel 1: Kern-Spiel-Loop & Wirtschaftssystem (ABGESCHLOSSEN)

**Status:** ✅ Abgeschlossen
**Commits:** 
- Initial commit mit Projektstruktur
- Core game loop with Pygame, city initialization, basic map rendering
- Trade system with buy/sell functionality and keyboard controls

**Implementiert:**
- Pygame Game Loop
- Schweizer Städte initialisiert (Zürich, Basel, Genf, Bern, Luzern)
- Handelssystem mit Kauf/Verkauf von Gütern
- Tastatursteuerung (1-3 für Handel in Städten)
- Nachrichtensystem

**Nächste Schritte:** Kapitel 2 beginnen

---

## Kapitel 2: Spionage & Rechtssystem

**Prompt für neue Session:**

```
Setze die Implementierung von Confoederatio Helvetica fort mit Kapitel 2: Spionage & Rechtssystem.

Kontext: Das Spiel ist eine Schweizer Wirtschaftssimulation im Renaissance-Stil, basierend auf Fugger II. Kapitel 1 (Kern-Spiel-Loop & Wirtschaftssystem) ist abgeschlossen.

Zu implementieren in diesem Kapitel:
1. Spionagesystem: Spieler können Spione auf Rivalen ansetzen, Beweise sammeln
2. Beweisbewertung: Verschiedene Beweistypen mit unterschiedlichem Wert
3. Gerichtsverfahren: Prozesse gegen Rivalen bei ausreichender Beweislage
4. Bestechungssystem: Richter bestechen für günstigeres Urteil (optional ein-/ausschaltbar)
5. Zeugen & Plädoyers im Gerichtsverfahren

Technische Details:
- Verwende die bestehende Projektstruktur in src/espionage/ und src/legal/
- Integriere das Spionagesystem mit dem bestehenden Spielzustand
- Füge UI-Elemente für Spionage-Missionen und Gerichtsverfahren hinzu
- Teste nach jedem implementierten Feature

Repository: https://github.com/Capricorn1000/confoederatio-helvetica
Branch: main
```

---

## Kapitel 3: Militärsystem & Kämpfe

**Prompt für neue Session:**

```
Setze die Implementierung von Confoederatio Helvetica fort mit Kapitel 3: Militärsystem & Kämpfe.

Kontext: Das Spiel ist eine Schweizer Wirtschaftssimulation im Renaissance-Stil, basierend auf Fugger II. Kapitel 1 und 2 sind abgeschlossen.

Zu implementieren in diesem Kapitel:
1. Schlachtensystem: Gefechte zwischen Truppen mit Schadensberechnung
2. Belagerungen: Festungsbelagerungen über mehrere Runden
3. Eskortierte Transporte: Schutz von Handelsgütern vor Räubern
4. KI-General-Steuerung: Computer übernimmt Führung bei ESC-Taste
5. Truppenverwaltung: Rekrutierung, Ausrüstung, Moral

Technische Details:
- Verwende die bestehende Projektstruktur in src/military/
- Integriere das Militärsystem mit dem bestehenden Spielzustand
- Füge UI-Elemente für Schlachten und Belagerungen hinzu
- Teste nach jedem implementierten Feature

Repository: https://github.com/Capricorn1000/confoederatio-helvetica
Branch: main
```

---

## Kapitel 4: Ereignisse & Abenteuer

**Prompt für neue Session:**

```
Setze die Implementierung von Confoederatio Helvetica fort mit Kapitel 4: Ereignisse & Abenteuer.

Kontext: Das Spiel ist eine Schweizer Wirtschaftssimulation im Renaissance-Stil, basierend auf Fugger II. Kapitel 1-3 sind abgeschlossen.

Zu implementieren in diesem Kapitel:
1. Historische Ereignisse: Jahr-für-Jahr Narrative der Schweizer Geschichte (Schwabenkrieg, Reformation, etc.)
2. Abenteuer/Sub-Plots: Über 30 "Spiele im Spiel" über mehrere Jahre hinweg
3. Zufallsmeldungen ("Schicksal"): Naturkatastrophen, Preisänderungen, etc.
4. Hilfesystem: Tipps von erfahrenen Kaufleuten basierend auf Spielzustand

Technische Details:
- Verwende die bestehende Projektstruktur in src/events/
- Integriere das Ereignissystem mit dem bestehenden Spielzustand
- Füge UI-Elemente für Ereignisse und Abenteuer hinzu
- Teste nach jedem implementierten Feature

Repository: https://github.com/Capricorn1000/confoederatio-helvetica
Branch: main
```

---

## Kapitel 5: UI Polish & Original Assets

**Prompt für neue Session:**

```
Setze die Implementierung von Confoederatio Helvetica fort mit Kapitel 5: UI Polish & Original Assets.

Kontext: Das Spiel ist eine Schweizer Wirtschaftssimulation im Renaissance-Stil, basierend auf Fugger II. Kapitel 1-4 sind abgeschlossen.

Zu implementieren in diesem Kapitel:
1. Integration der Original-Grafiken aus dem Fugger II Spiel (ICONS2/*.DAT Dateien)
2. Integration der Original-Soundeffekte (SMP22KHZ/*.DAT Dateien)
3. Integration der Original-Musik (MIDSONGS/*.MID Dateien)
4. Kartenansicht mit Schweizer Städten und Handelsrouten
5. Dialoge für Kauf/Verkauf, Gerichtsverfahren, etc.
6. Soundeffekte für verschiedene Aktionen

Original Assets Location: C:\Users\micha\Documents\Fugger_II\Fugger_II\FUGGER2\

Technische Details:
- Konvertiere die .DAT Icon-Dateien in ein von Pygame nutzbares Format
- Integriere MIDI-Musik mit pygame.mixer
- Füge Soundeffekte für Handel, Schlachten, etc. hinzu
- Teste nach jedem implementierten Feature

Repository: https://github.com/Capricorn1000/confoederatio-helvetica
Branch: main
```

---

## Kapitel 6: Mehrspieler & Final Polish

**Prompt für neue Session:**

```
Setze die Implementierung von Confoederatio Helvetica fort mit Kapitel 6: Mehrspieler & Final Polish.

Kontext: Das Spiel ist eine Schweizer Wirtschaftssimulation im Renaissance-Stil, basierend auf Fugger II. Kapitel 1-5 sind abgeschlossen.

Zu implementieren in diesem Kapitel:
1. Rundenbasiertes Mehrspieler-Spiel (Hotseat)
2. Spieler-Ankündigungen zwischen den Runden
3. Sound & Musik final integrieren und optimieren
4. Grafiken optimieren und polieren
5. Bugfixing & Testing
6. Dokumentation vervollständigen

Technische Details:
- Implementiere Mehrspieler-Support im Spielzustand
- Füge UI für Spielerwechsel hinzu
- Durchführe umfassendes Testing aller Features
- Optimiere Performance und Speicherbedarf

Repository: https://github.com/Capricorn1000/confoederatio-helvetica
Branch: main
```

---

## Allgemeine Hinweise für alle Kapitel

- **Sprache:** Alle Texte auf Deutsch (Standardsprache)
- **Code-Kommentare:** Können auf Englisch sein
- **Git Commits:** Auf Englisch mit klaren Beschreibungen
- **Tests:** Für alle kritischen Funktionen schreiben
- **Testing:** Nach jedem implementierten Feature testen