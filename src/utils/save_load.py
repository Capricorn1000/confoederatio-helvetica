"""
Speichern & Laden von Spielen.
"""

import json
import os


class SaveSystem:
    """Spiel-Speichersystem."""
    
    def __init__(self, save_directory="data/saves"):
        self.save_directory = save_directory
        os.makedirs(save_directory, exist_ok=True)
    
    def save_game(self, game_state, filename=None):
        """Spiel speichern."""
        if not filename:
            filename = f"save_{game_state.current_year}.json"
        
        filepath = os.path.join(self.save_directory, filename)
        
        state_dict = game_state.to_dict()
        with open(filepath, 'w') as f:
            json.dump(state_dict, f)
        
        return filepath
    
    def load_game(self, filename):
        """Spiel laden."""
        filepath = os.path.join(self.save_directory, filename)
        
        with open(filepath, 'r') as f:
            state_dict = json.load(f)
        
        return state_dict
    
    def list_saves(self):
        """Liste aller Speicherspiele zurückgeben."""
        if not os.path.exists(self.save_directory):
            return []
        
        return [f for f in os.listdir(self.save_directory) if f.endswith('.json')]