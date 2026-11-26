"""
Confoederatio Helvetica - Multiplayer Tests
Tests for hotseat gameplay, round switching, visibility rules,
and win conditions with multiple players.
"""

import unittest
from src.game_state import GameState


class TestMultiplayer(unittest.TestCase):
    """Test multiplayer scenarios."""
    
    def setUp(self):
        self.state = GameState()
        # Set up 4-player game
        self.state.players = [
            {"id": 1, "name": "Hans", "color": (255, 0, 0), "wealth": 1000},
            {"id": 2, "name": "Fritz", "color": (0, 255, 0), "wealth": 1000},
            {"id": 3, "name": "Anna", "color": (0, 0, 255), "wealth": 1000},
            {"id": 4, "name": "Greta", "color": (255, 255, 0), "wealth": 1000},
        ]
        self.state.current_player = 0
    
    def test_round_switching(self):
        """Test switching between player turns."""
        initial_player = self.state.players[self.state.current_player]["name"]
        self.assertEqual(initial_player, "Hans")
        
        # Advance to next player
        self.state.advance_turn()
        next_player = self.state.players[self.state.current_player]["name"]
        self.assertEqual(next_player, "Fritz")
        
        # Continue through all players
        for i in range(2, 4):
            self.state.advance_turn()
        final_player = self.state.players[self.state.current_player]["name"]
        self.assertEqual(final_player, "Greta")
    
    def test_year_advance(self):
        """Test that year advances after all players have played."""
        initial_year = self.state.year
        
        # All 4 players take their turns
        for _ in range(4):
            self.state.advance_turn()
        
        # Year should have advanced
        self.assertEqual(self.state.year, initial_year + 1)
    
    def test_player_visibility(self):
        """Test that players can only see relevant information."""
        player = self.state.players[0]
        
        # Player should see their own wealth
        self.assertIsNotNone(player["wealth"])
        
        # In hotseat, all info is visible (no fog of war in this implementation)
        for other_player in self.state.players:
            self.assertIsNotNone(other_player["name"])
    
    def test_win_condition_wealth(self):
        """Test wealth-based win condition."""
        # Set one player to have winning wealth
        self.state.players[1]["wealth"] = 50000
        self.state.win_threshold = 50000
        
        winner = self.state.check_win_condition()
        self.assertIsNotNone(winner)
        self.assertEqual(winner["name"], "Fritz")
    
    def test_no_winner_yet(self):
        """Test that no winner is declared when conditions not met."""
        winner = self.state.check_win_condition()
        self.assertIsNone(winner)


class TestGameBalance(unittest.TestCase):
    """Test game balance values."""
    
    def test_trade_prices_reasonable(self):
        """Verify trade prices are within reasonable range."""
        from src.game import Game
        game = Game()
        
        # Test various goods and routes
        for goods in ["grain", "wine", "cheese", "wool", "iron", "silver"]:
            price = game.calculate_trade_price(goods, "zuerich", "basel")
            self.assertGreater(price, 0)
            self.assertLess(price, 100)  # Reasonable upper bound
    
    def test_troop_costs_balanced(self):
        """Verify troop costs are balanced."""
        from src.game import Game
        game = Game()
        
        # Cavalry should be strongest and most expensive
        halberd_strength = game.calculate_troop_strength("halberdier", 10)
        crossbow_strength = game.calculate_troop_strength("crossbowman", 10)
        cavalry_strength = game.calculate_troop_strength("cavalry", 10)
        
        self.assertGreater(cavalry_strength, halberd_strength)
        self.assertGreater(halberd_strength, crossbow_strength)


if __name__ == '__main__':
    unittest.main()
