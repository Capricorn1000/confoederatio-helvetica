"""
Hauptspielfeld - Kartenansicht mit Schweizer Städten.
"""


class GameScreen:
    """Hauptspielfeld."""
    
    def __init__(self, game_state):
        self.game_state = game_state
    
    def run(self):
        """Spielschleife."""
        print("Confoederatio Helvetica - Spielfeld")
        print("=" * 40)
        
        while not self.game_state.game_over:
            self.display_info()
            
            choice = input("Aktion (1=Handel, 2=Bank, 3=Nächster Monat): ")
            
            if choice == "1":
                self.show_trade_menu()
            elif choice == "2":
                self.show_bank_menu()
            elif choice == "3":
                self.game_state.advance_month()
    
    def display_info(self):
        """Spielerinformationen anzeigen."""
        print(f"\nJahr: {self.game_state.current_year}")
        print(f"Geld: {self.game_state.player.cash:.2f} Gulden")
    
    def show_trade_menu(self):
        """Handelsmenü anzeigen."""
        print("Handelsmenü (noch nicht implementiert)")
    
    def show_bank_menu(self):
        """Bankmenü anzeigen."""
        print("Bankmenü (noch nicht implementiert)")