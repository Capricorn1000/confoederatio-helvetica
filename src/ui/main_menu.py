"""
Hauptmenü - Spielstart-Optionen.
"""


class MainMenu:
    """Hauptmenü des Spiels."""
    
    def __init__(self, game_state, config):
        self.game_state = game_state
        self.config = config
        self.options = ["Neues Spiel", "Fortsetzen", "Optionen", "Hilfe", "Beenden"]
    
    def run(self):
        """Menü-Schleife."""
        print("Confoederatio Helvetica - Hauptmenü")
        print("=" * 40)
        
        while True:
            for i, option in enumerate(self.options):
                print(f"{i+1}. {option}")
            
            choice = input("Wahl: ")
            
            if choice == "1":
                self.start_new_game()
                break
            elif choice == "2":
                self.continue_game()
                break
            elif choice == "3":
                self.show_options()
            elif choice == "4":
                self.show_help()
            elif choice == "5":
                print("Auf Wiedersehen!")
                break
    
    def start_new_game(self):
        """Neues Spiel starten."""
        print("Neues Spiel wird gestartet...")
    
    def continue_game(self):
        """Letztes Spiel fortsetzen."""
        print("Spiel wird geladen...")
    
    def show_options(self):
        """Optionen anzeigen."""
        print("Optionen-Menü (noch nicht implementiert)")
    
    def show_help(self):
        """Hilfe anzeigen."""
        print("Hilfe (noch nicht implementiert)")