#!/usr/bin/env python3
"""
Confoederatio Helvetica - Wirtschaftssimulation
Eine Schweizer Wirtschaftssimulation im Renaissance-Stil.

Startet das Spiel mit Pygame-Oberfläche.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config
from game_state import GameState
from ui.main_menu import MainMenu


def main():
    """Hauptfunktion des Spiels."""
    print("Confoederatio Helvetica - Wirtschaftssimulation")
    print("=" * 50)
    
    # Konfiguration laden
    config = Config()
    
    # Spielzustand initialisieren
    game_state = GameState(config)
    
    # Hauptmenü starten
    menu = MainMenu(game_state, config)
    menu.run()


if __name__ == "__main__":
    main()