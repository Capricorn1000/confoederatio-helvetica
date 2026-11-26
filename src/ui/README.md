# Benutzeroberfläche - Analyse & Spezifikation

## Original-Analyse (Fugger II)

Die Benutzeroberfläche von Fugger II ist typisch für DOS-Spiele der 1990er Jahre:
- SVGA-Grafiken mit UniVBE-Treiberunterstützung
- Mausgesteuerte Bedienung mit Menüs und Dialogen
- Kartenansicht mit Icons für Städte, Truppen und Transporte
- Soundeffekte und Musik (Soundkarte erforderlich)

### Grafische Elemente
- **Icons**: Verschiedene Icons für Städte, Güter, Truppen, etc.
- **Kartenansicht**: Übersichtskarte mit Belagerungen (gekreuzte goldene Schwerter)
- **Menüs**: Optionsmenü mit verschiedenen Einstellungen
- **Dialoge**: Für Kauf/Verkauf, Gerichtsverfahren, etc.

### Sound & Musik
- Soundeffekte für verschiedene Aktionen
- Hintergrundmusik während des Spiels
- Lautstärkeregelung im Optionsmenü

## Umsetzung in Confoederatio Helvetica (Pygame)

### Pygame-Architektur
```python
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        self.clock = pygame.time.Clock()
        self.running = True
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
            self.draw()
            
            self.clock.tick(60)
        
        pygame.quit()
```

### UI-Komponenten

#### 1. Hauptmenü (`main_menu.py`)
- Neues Spiel starten
- Letztes Spiel fortsetzen
- Optionen
- Hilfe/Handbuch
- Beenden

```python
class MainMenu:
    def __init__(self, game):
        self.game = game
        self.options = ["Neues Spiel", "Fortsetzen", "Optionen", "Hilfe", "Beenden"]
    
    def draw(self, screen):
        # Titelbildschirm mit Logo und Hintergrundgrafik
        pass
    
    def handle_input(self, event):
        # Maus- oder Tastatureingaben verarbeiten
        pass
```

#### 2. Spielfeld (`game_screen.py`)
- Kartenansicht mit Schweizer Städten
- Spielerinformationen (Geld, Güter, Truppen)
- Aktuelle Spielrunde/Jahr anzeigen
- Schnellzugriff auf wichtige Funktionen

```python
class GameScreen:
    def __init__(self, game):
        self.game = game
        self.map_view = MapView()
    
    def draw(self, screen):
        # Karte zeichnen
        self.map_view.draw(screen)
        
        # Spielerinformationen anzeigen
        self.draw_player_info(screen)
        
        # Aktuelle Runde/Jahr anzeigen
        self.draw_round_info(screen)
```

#### 3. Dialoge & Menüs (`dialogs.py`)
- Kauf/Verkauf-Dialoge
- Gerichtsverfahrens-Dialoge
- Spionage-Missionen konfigurieren
- Truppen verwalten

```python
class TradeDialog:
    def __init__(self, city, goods):
        self.city = city
        self.goods = goods
    
    def draw(self, screen):
        # Liste der verfügbaren Güter mit Preisen anzeigen
        pass
    
    def handle_purchase(self, good, quantity):
        # Kauf verarbeiten
        pass
```

#### 4. Kartenansicht (`map_view.py`)
- Schweizer Karte mit Städten und Handelsrouten
- Icons für Spielerposition, Truppen, Transporte
- Belagerungen anzeigen (gekreuzte goldene Schwerter)
- Zoom und Scroll-Funktionen

```python
class MapView:
    def __init__(self):
        self.cities = load_cities()
        self.routes = load_trade_routes()
    
    def draw(self, screen):
        # Karte zeichnen
        pass
    
    def get_city_at_position(self, x, y):
        # Stadt an Mausposition bestimmen
        pass
```

### Grafische Assets

#### Benötigte Grafiken
- **Hintergrundbilder**: Titelbildschirm, Spielfeldhintergrund
- **Icons**: Städte, Güter, Truppen, Transporte, Belagerungen
- **UI-Elemente**: Buttons, Menüs, Dialograhmen
- **Sprites**: Animationen für Transporte, Schlachten

#### Empfohlene Auflösung
- 1024x768 (Standard) oder 1280x960 (HD)
- Skalierbare Grafiken für verschiedene Bildschirmgrößen

### Sound & Musik

#### Pygame Audio
```python
import pygame.mixer

pygame.mixer.init()

# Soundeffekte laden
click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
trade_sound = pygame.mixer.Sound("assets/sounds/trade.wav")

# Hintergrundmusik abspielen
pygame.mixer.music.load("assets/music/background.ogg")
pygame.mixer.music.play(-1)  # Endlos loop
```

#### Benötigte Sounds
- Klick-Sound für Menüauswahl
- Handelssound für Kauf/Verkauf
- Schlachtensounds für Gefechte
- Hintergrundmusik (verschiedene Stimmungen)

### Optionen & Einstellungen

Das Optionsmenü sollte folgende Einstellungen bieten:
- **Grafik**: Auflösung, Farbmodus (256 Farben vs. 32768 Farben)
- **Sound**: Lautstärke, Soundkarte ein-/ausschalten
- **Spiel**: Spieldauer bis 1800, Bestechung ein-/aus, etc.
- **Steuerung**: Hotkeys konfigurieren

```python
class OptionsMenu:
    def __init__(self, game):
        self.game = game
        self.settings = load_settings()
    
    def save_settings(self):
        # Einstellungen speichern
        pass
```

## Technische Umsetzung

### Dateien
- `main_menu.py`: Hauptmenü mit Spielstart-Optionen
- `game_screen.py`: Hauptspielfeld mit Kartenansicht
- `dialogs.py`: Alle Dialoge und Menüs
- `map_view.py`: Kartenansicht mit Städten und Routen

### Datenstrukturen
```python
class UIElement:
    x: int
    y: int
    width: int
    height: int
    
class Button(UIElement):
    text: str
    action: callable
    
class Dialog(UIElement):
    title: str
    content: list[UIElement]
```

## Offene Fragen
1. Soll das Spiel im Fenstermodus oder Vollbild laufen?
2. Welche Auflösung soll standardmäßig verwendet werden?
3. Sollen moderne Grafiken verwendet werden oder Retro-Stil?
4. Wie komplex sollen die Animationen sein?